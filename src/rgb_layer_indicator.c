/*
 * RGB underglow layer indicator.
 *
 * Recolors the underglow to reflect the highest active layer. Layer 0 (BASE)
 * turns the underglow off; other layers use a per-layer color matching the
 * keycap-sticker palette.
 *
 * NOTE on split keyboards: layer-state events only fire on the CENTRAL half
 * (the peripheral does not run the keymap), and zmk_rgb_underglow_set_hsb() is
 * local to the side it runs on. So this lights the CENTRAL (left) half. Making
 * the peripheral (right) half follow needs syncing the active layer across the
 * split — see the follow-up note in the repo.
 */

#include <zephyr/kernel.h>
#include <zephyr/sys/util.h>

#include <zmk/event_manager.h>
#include <zmk/events/layer_state_changed.h>
#include <zmk/keymap.h>
#include <zmk/rgb_underglow.h>

/* index = layer number. h: 0-360, s/b: 0-100. Matches the sticker palette.
 * (Actual brightness is capped by CONFIG_ZMK_RGB_UNDERGLOW_BRT_MAX.) */
static const struct zmk_led_hsb layer_colors[] = {
    {.h = 0,   .s = 0,   .b = 0},    /* 0 BASE  - off            */
    {.h = 210, .s = 100, .b = 80},   /* 1 NUM   - blue           */
    {.h = 0,   .s = 100, .b = 80},   /* 2 SYM   - red            */
    {.h = 120, .s = 100, .b = 70},   /* 3 NAV   - green          */
    {.h = 270, .s = 100, .b = 80},   /* 4 FUN   - violet         */
};

static int rgb_layer_listener(const zmk_event_t *eh) {
    zmk_keymap_layer_index_t layer = zmk_keymap_highest_layer_active();

    if (layer == 0 || layer >= ARRAY_SIZE(layer_colors)) {
        zmk_rgb_underglow_off();
    } else {
        zmk_rgb_underglow_on();
        zmk_rgb_underglow_set_hsb(layer_colors[layer]);
    }

    return ZMK_EV_EVENT_BUBBLE;
}

ZMK_LISTENER(rgb_layer_indicator, rgb_layer_listener);
ZMK_SUBSCRIPTION(rgb_layer_indicator, zmk_layer_state_changed);
