# Custom C compiled into ZMK firmware via this config repo (a Zephyr module).
# Only built when the option below is enabled (see config/corne_choc_pro.conf).
if(CONFIG_ZMK_RGB_LAYER_INDICATOR)
  zephyr_library()
  zephyr_library_sources(src/rgb_layer_indicator.c)
endif()
