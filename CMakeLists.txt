# Compile our source INTO ZMK's `app` target (not a standalone zephyr_library),
# so it inherits ZMK's include paths (zmk/event_manager.h, zmk/keymap.h,
# zmk/rgb_underglow.h live in zmk/app/include, which a separate library doesn't see).
# This is the pattern ZMK modules use (e.g. caksoylar/zmk-rgbled-widget).
# Gated by the Kconfig option enabled in config/corne_choc_pro.conf.
target_sources_ifdef(CONFIG_ZMK_RGB_LAYER_INDICATOR app PRIVATE ${CMAKE_CURRENT_LIST_DIR}/src/rgb_layer_indicator.c)
