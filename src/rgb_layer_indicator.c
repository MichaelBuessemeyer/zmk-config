/*
 * RGB underglow layer indicator.
 *
 * Recolors the underglow to reflect the highest active layer (layer 0 = off),
 * matching the keycap-sticker palette. Compiled on the CENTRAL half only
 * (layer state lives on the central — see CMakeLists.txt).
 *
 * The central sets its own color via the local API. For the peripheral(s) it
 * pushes the equivalent rgb_ug behavior across the split (the only mechanism
 * that reaches the other half), so both halves show the layer color.
 */

#include <zephyr/kernel.h>
#include <zephyr/sys/util.h>
#include <zephyr/device.h>

#include <zmk/event_manager.h>
#include <zmk/events/layer_state_changed.h>
#include <zmk/keymap.h>
#include <zmk/rgb_underglow.h>
#include <dt-bindings/zmk/rgb.h>

#if IS_ENABLED(CONFIG_ZMK_SPLIT)
#include <zmk/behavior.h>
#include <zmk/split/central.h>
#endif

/* index = layer number. h:0-360, s/b:0-100. Matches the sticker palette.
 * (Actual brightness is capped by CONFIG_ZMK_RGB_UNDERGLOW_BRT_MAX.) */
static const struct zmk_led_hsb layer_colors[] = {
    {.h = 0,   .s = 0,   .b = 0},    /* 0 BASE  - off    */
    {.h = 210, .s = 100, .b = 80},   /* 1 NUM   - blue   */
    {.h = 0,   .s = 100, .b = 80},   /* 2 SYM   - red    */
    {.h = 120, .s = 100, .b = 70},   /* 3 NAV   - green  */
    {.h = 270, .s = 100, .b = 80},   /* 4 FUN   - violet */
};

#if IS_ENABLED(CONFIG_ZMK_SPLIT)
/* Push an rgb_ug command to every peripheral so the other half matches.
 * (Direct rgb_ug behavior dispatch is the only thing that crosses the split.) */
static void peripheral_rgb(uint32_t cmd, uint32_t val) {
    const struct device *rgb = DEVICE_DT_GET(DT_NODELABEL(rgb_ug));
    struct zmk_behavior_binding binding = {
        .behavior_dev = rgb->name,
        .param1 = cmd,
        .param2 = val,
    };
    struct zmk_behavior_binding_event event = {
        .position = 0,
        .timestamp = k_uptime_get(),
    };
    for (uint8_t s = 0; s < ZMK_SPLIT_CENTRAL_PERIPHERAL_COUNT; s++) {
        zmk_split_central_invoke_behavior(s, &binding, event, true);
    }
}
#else
static void peripheral_rgb(uint32_t cmd, uint32_t val) { ARG_UNUSED(cmd); ARG_UNUSED(val); }
#endif

static int rgb_layer_listener(const zmk_event_t *eh) {
    zmk_keymap_layer_index_t layer = zmk_keymap_highest_layer_active();

    if (layer == 0 || layer >= ARRAY_SIZE(layer_colors)) {
        zmk_rgb_underglow_off();              /* central / left */
        peripheral_rgb(RGB_OFF_CMD, 0);       /* peripheral / right */
    } else {
        struct zmk_led_hsb c = layer_colors[layer];
        uint32_t packed = ((uint32_t)c.h << 16) | ((uint32_t)c.s << 8) | (uint32_t)c.b;
        zmk_rgb_underglow_on();
        zmk_rgb_underglow_set_hsb(c);         /* central / left */
        peripheral_rgb(RGB_ON_CMD, 0);        /* peripheral on ... */
        peripheral_rgb(RGB_COLOR_HSB_CMD, packed); /* ... then colored */
    }
    return ZMK_EV_EVENT_BUBBLE;
}

ZMK_LISTENER(rgb_layer_indicator, rgb_layer_listener);
ZMK_SUBSCRIPTION(rgb_layer_indicator, zmk_layer_state_changed);
