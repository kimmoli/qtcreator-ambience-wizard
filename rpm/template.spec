Name:       harbour-ambience-%ProjectName%

Summary:    %Summary%
Version:    %Version%
Release:    1
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake
Vendor: %Vendor%
Packager: %Packager%

# This requirement is verboten for Harbour submission
Requires:   ambienced

%description
%Description%

%package ts-devel
Summary:   Translation source for %ProjectName% ambience
License:   TBD
Group:     System/GUI/Other

%description ts-devel
Translation source for a %ProjectName% ambience

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
# Without the root directory specified it will not be removed on uninstall
%{_datadir}/ambience/%{name}
%{_datadir}/ambience/%{name}/%{name}.ambience
%{_datadir}/ambience/%{name}/sounds.index
%{_datadir}/ambience/%{name}/images/*
%{_datadir}/ambience/%{name}/sounds/*
%{_datadir}/translations/%{name}_eng_en.qm

%files ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/%{name}.ts


# Scripts are verboten for Harbour submission, this is only needed for
# install methods _other_ than the Store.
%post
systemctl-user restart ambienced.service

