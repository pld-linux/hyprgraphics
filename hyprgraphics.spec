Summary:	Hyprland graphics / resource utilities
Name:		hyprgraphics
Version:	0.1.1
Release:	3
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/hyprwm/hyprgraphics/releases
Source0:	https://github.com/hyprwm/hyprgraphics/archive/v%{version}/%{name}-v%{version}.tar.gz
# Source0-md5:	e7be69a12ad3954819f4599779862366
Patch0:		flags.patch
URL:		https://hyprland.org/
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 3.30
BuildRequires:	hyprutils-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel
BuildRequires:	libmagic-devel
BuildRequires:	libstdc++-devel >= 6:14
BuildRequires:	libwebp-devel
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hyprgraphics is a small C++ library with graphics / resource related
utilities used across the hypr* ecosystem.

%package devel
Summary:	Header files for hyprgraphics
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for hyprgraphics.

%prep
%setup -q
%patch -P 0 -p1

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libhyprgraphics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhyprgraphics.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhyprgraphics.so
%{_includedir}/hyprgraphics
%{_pkgconfigdir}/hyprgraphics.pc
