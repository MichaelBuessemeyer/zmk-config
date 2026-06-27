# Compile our source INTO ZMK's `app` target (not a standalone zephyr_library),
# so it inherits ZMK's include paths (zmk/event_manager.h, zmk/keymap.h,
# zmk/rgb_underglow.h live in zmk/app/include, which a separate library doesn't see).
# This is the pattern ZMK modules use (e.g. caksoylar/zmk-rgbled-widget).
#
# Compile it ONLY on the central half: zmk_keymap_highest_layer_active() and the
# layer_state_changed event are central-only symbols, so the peripheral build
# would fail to link them. (The peripheral can't observe layer state anyway.)
# Gated by the Kconfig option enabled in config/corne_choc_pro.conf.
if(CONFIG_ZMK_RGB_LAYER_INDICATOR AND (CONFIG_ZMK_SPLIT_ROLE_CENTRAL OR NOT CONFIG_ZMK_SPLIT))
  target_sources(app PRIVATE ${CMAKE_CURRENT_LIST_DIR}/src/rgb_layer_indicator.c)
endif()
