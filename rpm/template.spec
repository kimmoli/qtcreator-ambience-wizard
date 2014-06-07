Name:       ambience-%ProjectName%

Summary:    %Summary%
Version:    %Version%
Release:    1
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake

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

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post



%files
%defattr(-,root,root,-)
%{_datadir}/ambience/ambience-%ProjectName%/ambience-%ProjectName%.ambience
%{_datadir}/ambience/ambience-%ProjectName%/sounds.index
%{_datadir}/ambience/ambience-%ProjectName%/images/*
%{_datadir}/ambience/ambience-%ProjectName%/sounds/*
%{_datadir}/translations/ambience-%ProjectName%_eng_en.qm

%files -n ambience-%ProjectName%-ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/ambience-%ProjectName%.ts
