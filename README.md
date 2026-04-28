# Google Maps Android Appium Test

Automatizovaný UI test pro nativní aplikaci Google Maps na platformě Android.

Test vyhledá místo `Packeta Group` v aplikaci Google Maps a ověří, že zobrazený výsledek obsahuje správný název a adresu.

## Testovací scénář

Test automatizuje následující kroky:

1. Spuštění aplikace Google Maps na Android emulátoru.
2. Interakce s vyhledávacím polem.
3. Zadání textu `Packeta Group`.
4. Výběr výsledku z našeptávače.
5. Vyčkání na načtení detailu vyhledaného místa.
6. Ověření, že výsledek obsahuje název `Packeta Group` nebo `Packeta s.r.o.`.
7. Ověření, že detail místa obsahuje adresu `Českomoravská 2408, 190 00 Praha 9-Libeň`.

## Použité technologie

- Python
- pytest
- Appium
- Appium Python Client
- UiAutomator2
- Android Emulator
- Page Object Model

## Struktura projektu

```text
google-maps-appium-test/
├── helpers/
│   ├── __init__.py
│   └── capabilities.py
├── pages/
│   ├── __init__.py
│   ├── google_maps_page.py
│   └── place_detail_page.py
├── tests/
│   ├── __init__.py
│   └── test_google_maps_search.py
├── reports/
├── requirements.txt
└── README.md
````

Soubory `__init__.py` jsou součástí projektu, aby Python správně rozpoznal složky `helpers`, `pages` a `tests` jako importovatelné balíčky.

## Prerekvizity

Před spuštěním testu je potřeba mít nainstalované:

* Python 3.13+
* Node.js a npm
* Appium
* Appium UiAutomator2 driver
* Android Studio
* Android SDK
* Android Emulator
* Google Maps v emulátoru
* Aktivní Android emulátor dostupný přes `adb`

## Instalace Node.js

### macOS

Doporučená varianta je instalace přes `nvm`:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.zshrc
nvm install --lts
nvm use --lts
```

Ověření:

```bash
node -v
npm -v
```

### Windows

Stáhněte a nainstalujte **Node.js LTS** z oficiální stránky:

```text
https://nodejs.org
```

Po instalaci otevřete nový PowerShell nebo Command Prompt a ověřte:

```powershell
node -v
npm -v
```

### Linux

Doporučená varianta je instalace přes `nvm`:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm use --lts
```

Ověření:

```bash
node -v
npm -v
```

## Instalace Appia

Appium se instaluje přes npm.

### macOS / Linux

```bash
npm install -g appium
```

### Windows

```powershell
npm install -g appium
```

Ověření instalace:

```bash
appium -v
```

Na Windows použijte v PowerShellu stejný příkaz:

```powershell
appium -v
```

Instalace Android driveru pro Appium:

```bash
appium driver install uiautomator2
```

Na Windows:

```powershell
appium driver install uiautomator2
```

Ověření nainstalovaných driverů:

```bash
appium driver list --installed
```

Ve výpisu by měl být dostupný driver:

```text
uiautomator2
```

## Instalace Android Studia a Android SDK

### macOS

Nainstalujte Android Studio z:

```text
https://developer.android.com/studio
```

Po prvním spuštění projděte Setup Wizard a nainstalujte:

* Android SDK
* Android SDK Platform-Tools
* Android Emulator
* Android SDK Command-line Tools

Nastavení proměnných prostředí v `~/.zshrc`:

```bash
echo 'export ANDROID_HOME=$HOME/Library/Android/sdk' >> ~/.zshrc
echo 'export ANDROID_SDK_ROOT=$HOME/Library/Android/sdk' >> ~/.zshrc
echo 'export PATH=$PATH:$ANDROID_HOME/platform-tools' >> ~/.zshrc
echo 'export PATH=$PATH:$ANDROID_HOME/emulator' >> ~/.zshrc
source ~/.zshrc
```

Ověření:

```bash
adb version
emulator -version
```

### Windows

Nainstalujte Android Studio z:

```text
https://developer.android.com/studio
```

Po prvním spuštění projděte Setup Wizard a nainstalujte:

* Android SDK
* Android SDK Platform-Tools
* Android Emulator
* Android SDK Command-line Tools

Typická cesta k Android SDK na Windows je:

```text
C:\Users\<USER>\AppData\Local\Android\Sdk
```

Nastavte systémové proměnné prostředí:

```text
ANDROID_HOME=C:\Users\<USER>\AppData\Local\Android\Sdk
ANDROID_SDK_ROOT=C:\Users\<USER>\AppData\Local\Android\Sdk
```

Do systémové proměnné `Path` přidejte:

```text
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\emulator
```

Poté otevřete nový PowerShell a ověřte:

```powershell
adb version
emulator -version
```

### Linux

Nainstalujte Android Studio z:

```text
https://developer.android.com/studio
```

Po prvním spuštění projděte Setup Wizard a nainstalujte:

* Android SDK
* Android SDK Platform-Tools
* Android Emulator
* Android SDK Command-line Tools

Typická cesta k Android SDK na Linuxu je:

```text
$HOME/Android/Sdk
```

Nastavení proměnných prostředí v `~/.bashrc`:

```bash
echo 'export ANDROID_HOME=$HOME/Android/Sdk' >> ~/.bashrc
echo 'export ANDROID_SDK_ROOT=$HOME/Android/Sdk' >> ~/.bashrc
echo 'export PATH=$PATH:$ANDROID_HOME/platform-tools' >> ~/.bashrc
echo 'export PATH=$PATH:$ANDROID_HOME/emulator' >> ~/.bashrc
source ~/.bashrc
```

Ověření:

```bash
adb version
emulator -version
```

## Android emulátor

Emulátor je možné vytvořit v Android Studiu přes:

```text
Android Studio → Device Manager → Create Device
```

Doporučené nastavení:

```text
Device: běžný Pixel profil, například Pixel 7, Pixel 8 nebo podobný
System image: Google Play image
Architecture:
- macOS Apple Silicon: arm64-v8a
- Windows/Linux Intel/AMD: x86_64
```

Po spuštění emulátoru ověřte, že je dostupný přes ADB.

### macOS / Linux

```bash
adb devices
```

### Windows

```powershell
adb devices
```

Očekávaný výstup:

```text
List of devices attached
emulator-5554   device
```

Ověření, že je nainstalovaná aplikace Google Maps:

### macOS / Linux

```bash
adb shell pm list packages | grep maps
```

### Windows PowerShell

```powershell
adb shell pm list packages | Select-String maps
```

Očekávaný výstup:

```text
package:com.google.android.apps.maps
```

Ruční spuštění Google Maps:

```bash
adb shell monkey -p com.google.android.apps.maps 1
```

Na Windows:

```powershell
adb shell monkey -p com.google.android.apps.maps 1
```

## Doporučené nastavení emulátoru

Pro stabilnější běh UI testů je vhodné vypnout animace.

### macOS / Linux / Windows

```bash
adb shell settings put global window_animation_scale 0
adb shell settings put global transition_animation_scale 0
adb shell settings put global animator_duration_scale 0
```

Na Windows lze stejné příkazy spustit v PowerShellu.

## Instalace Python závislostí

### macOS / Linux

Ve složce projektu vytvořte virtuální prostředí:

```bash
python3 -m venv .venv
```

Aktivace virtuálního prostředí:

```bash
source .venv/bin/activate
```

Instalace závislostí:

```bash
pip install -r requirements.txt
```

Pokud `requirements.txt` ještě neexistuje, lze závislosti nainstalovat ručně:

```bash
pip install Appium-Python-Client pytest pytest-html
```

A následně uložit:

```bash
pip freeze > requirements.txt
```

### Windows PowerShell

Ve složce projektu vytvořte virtuální prostředí:

```powershell
python -m venv .venv
```

Aktivace virtuálního prostředí:

```powershell
.\.venv\Scripts\Activate.ps1
```

Pokud PowerShell blokuje spuštění aktivačního skriptu, spusťte:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Poté znovu aktivujte prostředí:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalace závislostí:

```powershell
pip install -r requirements.txt
```

Pokud `requirements.txt` ještě neexistuje:

```powershell
pip install Appium-Python-Client pytest pytest-html
pip freeze > requirements.txt
```

## Spuštění Appium serveru

Před spuštěním testu musí běžet Appium server.

### macOS / Linux

V samostatném terminálu spusťte:

```bash
appium
```

### Windows PowerShell

```powershell
appium
```

Server standardně běží na adrese:

```text
http://127.0.0.1:4723
```

Tento terminál nechte běžet po celou dobu testu.

## Spuštění testu

### macOS / Linux

V druhém terminálu přejděte do root složky projektu:

```bash
cd ~/Projects/google-maps-appium-test
```

Aktivujte virtuální prostředí:

```bash
source .venv/bin/activate
```

Spusťte test:

```bash
pytest -v
```

### Windows PowerShell

V druhém terminálu přejděte do root složky projektu, například:

```powershell
cd C:\Users\<USER>\Projects\google-maps-appium-test
```

Aktivujte virtuální prostředí:

```powershell
.\.venv\Scripts\Activate.ps1
```

Spusťte test:

```powershell
pytest -v
```

## Spuštění testu s HTML reportem

### macOS / Linux

Pro vytvoření HTML reportu s unikátním názvem spusťte:

```bash
mkdir -p reports
pytest -v --html=reports/report_$(date +"%Y-%m-%d_%H-%M-%S").html --self-contained-html
```

### Windows PowerShell

Pro vytvoření HTML reportu s unikátním názvem spusťte:

```powershell
New-Item -ItemType Directory -Force -Path reports
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
pytest -v --html="reports/report_$timestamp.html" --self-contained-html
```

Report se uloží například jako:

```text
reports/report_2026-04-28_11-42-10.html
```

Test zároveň ukládá screenshot poslední obrazovky po každém běhu do složky `reports/`.

Screenshoty se také ukládají s timestampem, například:

```text
reports/final_screen_2026-04-28_11-42-10.png
```

Poznámka: pokud se test spouští přes PyCharm tlačítkem **Run**, timestamp v názvu HTML reportu se automaticky nepoužije. Pro vytvoření timestampovaného HTML reportu je potřeba spustit výše uvedený příkaz z terminálu.

## Appium capabilities

Test používá následující Appium nastavení:

```python
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Android Emulator"
options.app_package = "com.google.android.apps.maps"
options.app_activity = "com.google.android.maps.MapsActivity"
options.no_reset = True
options.new_command_timeout = 120
```

Aplikace Google Maps je před testem restartována pomocí:

```python
driver.terminate_app("com.google.android.apps.maps")
driver.activate_app("com.google.android.apps.maps")
```

Díky tomu test začíná konzistentněji i v případě, že byla aplikace před spuštěním testu otevřená.

## Architektura řešení

Projekt používá návrhový vzor Page Object Model.

### `helpers/capabilities.py`

Obsahuje konfiguraci Appium session pro Android a Google Maps.

Konfigurace určuje:

* platformu Android,
* driver UiAutomator2,
* package Google Maps,
* startovací activity,
* `no_reset=True`,
* `new_command_timeout=120`.

### `pages/google_maps_page.py`

Obsahuje logiku pro práci s vyhledáváním v Google Maps.

Metoda `search_for()`:

1. najde vyhledávací pole,
2. klikne do něj,
3. vymaže případný původní obsah,
4. zadá hledaný text,
5. vybere odpovídající výsledek z našeptávače.

Vyhledávací pole se nejprve otevírá přes prvek:

```text
com.google.android.apps.maps:id/search_omnibox_text_box
```

Poté se pro zadání textu používá skutečné editovatelné pole:

```text
com.google.android.apps.maps:id/search_omnibox_edit_text
```

Výsledek z našeptávače se hledá uvnitř kontejneru:

```text
com.google.android.apps.maps:id/typed_suggest_container
```

Pokud se našeptávač nepodaří najít, test použije fallback přes Android Enter keycode `66`.

### `pages/place_detail_page.py`

Obsahuje logiku pro práci s detailem místa.

Metoda `get_place_name()`:

* najde kartu místa podle `business_place_card`,
* uvnitř ní hledá `TextView`, který obsahuje `Packeta`,
* vrátí text názvu místa.

Metoda `get_place_address()`:

* ověří, zda je adresa dostupná,
* v případě potřeby scrolluje obrazovkou,
* hledá adresu v detailu místa,
* vrátí text adresy.

Scrollování je implementováno přes Appium mobile gesture:

```python
driver.execute_script("mobile: scrollGesture", ...)
```

Velikost scrollovací oblasti se počítá podle velikosti obrazovky emulátoru.

### `tests/test_google_maps_search.py`

Obsahuje samotný testovací scénář.

Test:

1. vytvoří Appium driver,
2. restartuje Google Maps,
3. vyhledá `Packeta Group`,
4. načte název místa,
5. načte adresu,
6. ověří název,
7. ověří adresu,
8. uloží screenshot poslední obrazovky,
9. ukončí Appium session.

## Stabilita testu

Test nepoužívá pevné čekání typu `sleep`.

Místo toho používá explicitní čekání pomocí:

```python
WebDriverWait
expected_conditions
```

Test také používá konkrétní Android UI selektory podle:

* `resourceId`,
* `className`,
* `text`,
* `textContains`,
* `descriptionContains`.

Pro případ, kdy adresa není ihned viditelná, test scrolluje obrazovkou a opakovaně hledá adresní prvek.

## Známé limity

Google Maps je aplikace třetí strany, proto může být test ovlivněn:

* verzí aplikace Google Maps,
* jazykem zařízení,
* stavem přihlášení,
* oprávněními,
* onboarding dialogy,
* historií vyhledávání,
* změnami UI ze strany Googlu,
* aktuálním stavem aplikace při startu testu.

Z tohoto důvodu test používá explicitní čekání, restart aplikace před testem, scrollování a fallback při výběru výsledku z našeptávače.

## Očekávaný výsledek

Při úspěšném běhu by měl výstup obsahovat:

```text
tests/test_google_maps_search.py::test_google_maps_search PASSED
```

Test ověřuje:

```text
Packeta Group nebo Packeta s.r.o.
Českomoravská 2408, 190 00 Praha 9-Libeň
```

```
```
