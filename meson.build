project('pardus-about')

subdir('po')
subdir('debian')

# install sources
install_subdir('src', install_dir : '/usr/share/pardus/pardus-about')
install_subdir('data', install_dir : '/usr/share/pardus/pardus-about')
install_subdir('ui', install_dir : '/usr/share/pardus/pardus-about')
install_subdir('css', install_dir : '/usr/share/pardus/pardus-about')
install_subdir('data/icons', install_dir : '/usr/share/icons/hicolor/scalable/devices', strip_directory: true)

# icons
install_data('pardus-hardware-info.svg', install_dir : '/usr/share/icons/hicolor/scalable/apps')
install_data('pardus-about.svg', install_dir : '/usr/share/icons/hicolor/scalable/apps')
install_data('pardus-about-symbolic.svg', install_dir : '/usr/share/icons/hicolor/scalable/apps')

# polkit rule
install_data('tr.org.pardus.pkexec.pardus-about.policy', install_dir : '/usr/share/polkit-1/actions/')

# desktop files
install_data('tr.org.pardus.about.desktop', install_dir : '/usr/share/applications/')
install_data('tr.org.pardus.about-hardware.desktop', install_dir : '/usr/share/applications/')

# command
install_data('pardus-about.py', install_dir : '/usr/bin', rename: 'pardus-about')

