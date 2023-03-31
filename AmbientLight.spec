Name:		AmbientLight
Summary:	Ambient light controller, primarily for Plasma Mobile
Version:	0.0.1
Release:	2
License:	GPLv3
Source0:	https://github.com/OpenMandrivaSoftware/AmbientLight/archive/refs/tags/%{version}.tar.gz
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Sensors)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5

%description
Ambient light controller, primarily for Plasma Mobile

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
cat >%{buildroot}%{_sysconfdir}/xdg/autostart/ch.lindev.ambientlight.desktop <<'EOF'
[Desktop Entry]
Type=Application
Icon=ambient-light
Name=Ambient Light
Exec=%{_bindir}/ambient-light
NoDisplay=true
X-KDE-autostart-phase=2
EOF

%files
%{_bindir}/ambient-light
%{_sysconfdir}/xdg/autostart/ch.lindev.ambientlight.desktop
