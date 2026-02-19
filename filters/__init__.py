from .instagram import *
from .artistic import *
from .distortion import *
from .retro import *
from .color_moods import *
from .blurs import *
from .light import *
from .reflections import *
from .tech import *
from .beauty import *

FILTERS = [
    ("Original", filter_original),

    # Instagram Classics
    ("Clarendon", filter_clarendon),
    ("Gingham", filter_gingham),
    ("Juno", filter_juno),
    ("Lark", filter_perpetua), 
    ("Reyes", filter_reyes),
    
    # More Instagram
    ("Aden", filter_aden),
    ("Brooklyn", filter_brooklyn),
    ("Earlybird", filter_earlybird),
    ("Hudson", filter_hudson),
    ("Inkwell", filter_inkwell),
    ("Lo-Fi", filter_lofi),
    ("Nashville", filter_nashville),
    ("Rise", filter_rise),
    ("Valencia", filter_valencia),
    ("Walden", filter_walden),
    ("Amaro", filter_amaro),
    ("Brannan", filter_brannan),
    ("Hefe", filter_hefe),
    ("Toaster", filter_toaster),
    ("Maven", filter_maven),
    ("Vesper", filter_vesper),
    ("Chrome", filter_chrome),
    
    # Classic Styles
    ("1977", filter_1977),
    ("Kelvin", filter_kelvin),
    ("Slumber", filter_slumber),
    ("Sutro", filter_sutro),
    ("Moon (B&W)", filter_moon),
    ("X-Pro II", filter_xpro),
    ("Mayfair", filter_mayfair),

    
    # Creative Filters
    ("Sepia", filter_sepia),
    ("Polaroid", filter_polaroid),
    ("Vintage", filter_vintage),
    ("Retro 80s", filter_retro),
    ("Lomo", filter_lomo),
    
    # Seasonal
    ("Summer", filter_summer),
    ("Autumn", filter_autumn),
    ("Winter", filter_winter),
    ("Spring", filter_spring),
    
    # Time of Day
    ("Blue Hour", filter_blue_hour),
    
    # Cinematic
    ("Cinematic Teal-Orange", filter_cinematic_teal_orange),
    ("Cross Process", filter_cross_process),
    ("Bleach Bypass", filter_bleach_bypass),
    ("Dramatic", filter_dramatic),
    ("Noir", filter_noir),
    ("Tokyo Nights", filter_tokyo),
    
    # Artistic
    ("Sketch", filter_sketch),
    ("Cartoon", filter_cartoon),
    ("Pop Art", filter_pop_art),
    ("Emboss", filter_emboss),
    
    # Tech/Digital
    ("Cyberpunk", filter_cyberpunk),

    ("Thermal", filter_thermal),
    ("Infrared", filter_infrared),
    ("Night Vision", filter_night_vision),
    
    # Glitch/Retro Tech
    ("Glitch", filter_glitch),
    ("RGB Split", filter_rgb_split),
    ("Digital Corrupt", filter_digital_corrupt),
    ("Pixelate", filter_pixelate),
    ("TV Static", filter_tv_static),
    
    # Color Moods
    ("Pastel Dream", filter_pastel_dream),
    ("Cotton Candy", filter_cotton_candy),
    ("Sunset Vibes", filter_sunset_vibes),
    ("Neon Glow", filter_neon_glow),
    ("Moody Blues", filter_moody_blues),
    ("Soft Focus", filter_soft_focus),
    
    # Nature Themes
    ("Arctic", filter_arctic),
    ("Desert", filter_desert),
    ("Forest", filter_forest),
    ("Fire", filter_fire),
    ("Ice", filter_ice),
    
    # Trendy Colors
    ("Lavender", filter_lavender),
    ("Mint", filter_mint),
    ("Peach", filter_peach),
    ("Rose Gold", filter_rose_gold),
    
    # Distortions
    ("Mirror", filter_mirror_horizontal),
    ("Fisheye", filter_fisheye),
    ("Swirl", filter_swirl),
    
    # Beauty
    ("Soft Skin", filter_soft_skin),

    
    # Distortions (Extended)
    ("Bulge", filter_bulge),
    ("Pinch", filter_pinch),
    ("Ripple", filter_ripple),
    ("Twist", filter_twist),
    ("Perspective Tilt", filter_perspective_tilt),
    
    # Blurs
    ("Motion Blur", filter_motion_blur),
    ("Radial Blur", filter_radial_blur),
    ("Tilt Shift", filter_tilt_shift),
    
    # Reflections
    ("Vertical Flip", filter_vertical_flip),
    ("Quad Mirror", filter_quad_mirror),
    ("Glass Window", filter_glass_window),
    
    # Light & Lens

    ("Bloom", filter_bloom),
    ("Light Leak", filter_light_leak),
    
    # Color & Texture
    ("Negative", filter_negative),
    ("Posterize", filter_posterize),
    ("Film Dust", filter_film_dust_scratches),
]
