%define oname uiadbus

Name:     	mono-%{oname}
Version:	2.0
Release:	%mkrel 1
License:	MIT or X11
URL:		http://www.mono-a11y.org/
Source0:	http://mono-a11y.org/releases/2.0/sources/%{oname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	mono-devel >= 2.4
BuildRequires:	mono-uia >= 2.0
BuildRequires:	glib-sharp2 >= 2.12.8
BuildRequires:	ndesk-dbus > 0.0.6
Summary:	UiaDbus Types and Interfaces
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Types and interfaces used to expose Winforms and Moonlight apps to
UIAutomationClient.

%prep
%setup -q -n %{oname}-%{version}

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib \
	--enable-external-ndesk-dbus
make

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %buildroot%_datadir/pkgconfig
mv %buildroot%_prefix/lib/pkgconfig/*.pc %buildroot%_datadir/pkgconfig/

%clean
rm -rf %buildroot

%files
%defattr(-, root, root)
%_prefix/lib/uiadbus
%_datadir/pkgconfig/*.pc
%_prefix/lib/mono/accessibility/UiaDbus.dll
%_prefix/lib/mono/gac/*
