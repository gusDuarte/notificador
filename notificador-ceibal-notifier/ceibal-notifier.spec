Name:		ceibal-notifier
Version:	1.0
Release:	1.uy
Summary:	Librerias Ceibal para las notificaciones de las XO

License:	GPLv2+
URL:		https://desarrollo.ceibal.edu.uy
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Requires:		python, python-ceibal-libxo >= 2.0


%description
Notificador Ceibal. Obtiene notificaciones desde el servidor escolar y las 
muestra integrandose con el sistema de notificaciones de dbus.

%prep
%setup -q

%install
#rm -rf $RPM_BUILD_ROOT DESTDIR=%{buildroot}
mkdir -p $RPM_BUILD_ROOT%{python_sitelib}/ceibal/
cp -r notifier $RPM_BUILD_ROOT%{python_sitelib}/ceibal/
chmod -R 755 $RPM_BUILD_ROOT%{python_sitelib}/ceibal/notifier/
#mkdir -p $RPM_BUILD_ROOT/etc/cron.d
#echo "*/5 * * * * root python /usr/sbin/actualizador.py" > $RPM_BUILD_ROOT/etc/cron.d/actualizador
mkdir -p $RPM_BUILD_ROOT%{_sbindir}/
install -m 755 sbin/notificador $RPM_BUILD_ROOT%{_sbindir}/notificador
mkdir -p $RPM_BUILD_ROOT/etc/notifier/{data,images}/
mkdir -p $RPM_BUILD_ROOT/etc/notifier/data/tmp/
#install -d -m 755 images $RPM_BUILD_ROOT/etc/notifier/
cp images/* $RPM_BUILD_ROOT/etc/notifier/images/
chmod -R 777 $RPM_BUILD_ROOT/etc/notifier/
mkdir -p $RPM_BUILD_ROOT/etc/cron.d/
install -m 644 cron/notifier $RPM_BUILD_ROOT/etc/cron.d/
install -m 777 messages.db $RPM_BUILD_ROOT/etc/notifier/data

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/ceibal/notifier/
%{_sbindir}/notificador
/etc/notifier/data/tmp/
/etc/notifier/images/
/etc/cron.d/notifier
/etc/notifier/data/messages.db

%changelog
* Wed Jun 13 2012 ebordon <ebordon@plan.ceibal.edu.uy> - 0.6-2
- Se modifica la clase Store para que desde la actividad puedan marcar favoritos

* Thu Mar 8 2012 dcastelo <dcastelo@plan.ceibal.edu.uy> - 0.6-1
- Se agrega base de datos de mensajes como parte del rpm

* Fri Dec 16 2011 ebordon <ebordon@plan.ceibal.edu.uy> - 0.5-2
- Cambia la ruta donde se guardan los mensajes. 
- Se agrega llamado a store en el cron

* Tue Dec 13 2011 ebordon <ebordon@plan.ceibal.edu.uy> - 0.5-1
- Implementación compatible con F14 (Sugar y Gnome) y Ubuntu 10.04

* Thu Jan 20 2011 ebordon <ebordon@plan.ceibal.edu.uy> - 0.3
- Agrega filtro de fechas

* Thu Jan 20 2011 ebordon <ebordon@plan.ceibal.edu.uy> - 0.2
- Agrega directorio de imagenes

* Thu Jan 20 2011 ebordon <ebordon@plan.ceibal.edu.uy> - 0.1
- Versión inicial
