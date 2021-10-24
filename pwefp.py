#!usr/bin/python3
import os, time, signal, sys,subprocess
from sys import stdout
option = int
selectying = str
def sig_handler(sig, frame):
    red()
    print("\n\n\033[1;33m[+] \033[1;31mUsted ha abortado la instalación!!!\033[1;33m [+]")
    sys.exit(1)

signal.signal(signal.SIGINT, sig_handler)

def whatOS():
    global OperatingSystem
    if True:
        OperatingSystem=os.popen("lsb_release -a 2>/dev/null | grep 'Contributor ID:' | awk '{print$3}").read()
        #OS = subprocess.run("whatOS=$(lsb_release -a | grep 'Distributor ID:') 2>/dev/null")
        print(OperatingSystem)
    #else:
        #os.system("whatOS=$(uname -a | awk '{print$2}')")
    return OperatingSystem

whatOS()

def PrintOS():
    global selectying
    global OS
    print("\033[1;33mSi su Sistema Operativo es\033[1;35m : \n\n\033[1;34mKali   \033[1;35m:\033[1;33m Presione 1\n\033[1;34mParrot \033[1;35m:\033[1;33m Presione 2\n\033[1;34mArch\033[1;35m   : \033[1;33mPresione 3\n")
    OS = input("-->    \033[1;35m: \033[1;33m")

    if OS == '1':
        selectying = "Kali Linux"
    elif OS == '2':
        selectying = str("Parrot OS")
    elif OS == '3':
        selectying = str("Arch Linux")
    else:
        print("Por favor seleccione una opción del 1 al 3:")
        while OS != '1' or '2' or '3':
        #while selectying != "Kali Linux" or "Parrot OS" or "Arch Linux":
            OS=
            PrintOS()    
    print(f"\n\033[1;33mSelecciono\033[1;35m : \033[1;34m{selectying}")
    #menu()

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def cyan():
    CYAN = "\033[1;36m"
    stdout.write(CYAN)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)
banner = """
(CREDITOS A YORKOX https://github.com/yorkox0/autoBspwm)"""
def banner1():
    cyan()
    print("""
    ██████╗ ██╗    ██╗   ███████╗   ███████╗██████╗ 
    ██╔══██╗██║    ██║   ██╔════╝   ██╔════╝██╔══██╗
    ██████╔╝██║ █╗ ██║   █████╗     █████╗  ██████╔╝
    ██╔═══╝ ██║███╗██║   ██╔══╝     ██╔══╝  ██╔═══╝ 
    ██║██╗  ╚███╔███╔╝██╗███████╗██╗██║██╗  ██║██╗  
    ╚═╝╚═╝   ╚══╝╚══╝ ╚═╝╚══════╝╚═╝╚═╝╚═╝  ╚═╝╚═╝  

    Professional Work Environment For Pentesting {}""".format("\033[1;37m({Style S4vitar)}\033[0m"))
banner2 = """\n({<-- No ejecutar el script como root -->})\n"""
banner3 = ("""\n Su sistema operativo es: \033[1;34m{}""".format(OperatingSystem))
def menu():
    red()
    print(banner)
    cyan()
    banner1()
    red()
    print(banner2)
    yellow()
    time.sleep(0.2)
    print("1 -> Instalar Requerimientos necesarios")
    time.sleep(0.2)
    print("\n2 -> Instalar Bspwm")
    time.sleep(0.2)
    print("\n3 -> Instalar Polybar, Picom, Rofi...")
    time.sleep(0.2)
    print("\n4 -> Acelerar el arranque del sistema operativo")
    time.sleep(0.2)
    print("\n5 -> Instalar Todo")
    time.sleep(0.2)
    print("\n6 -> Salir")
    time.sleep(0.2)
    print(banner3," '\033[1;31m'¡Si no es asi!'\033[1;33m' Presione 7 para cambiar su sistema operativo")

    option = int(input("\n--> Seleccione una opción: "))

    if option == 1:
        red()
        print("\nEligio: 1 -> Instalar Requerimientos necesarios\n")
        requirements()
    elif option == 2:
        red()
        print("\nEligio: 2 -> Instalar bspwm\n")
        bspwm()
    elif option == 3:
        red()
        print("\nEligio: 3 -> Instalar Polybar, Picom, Rofi...\n")
        polybar()
    elif option == 4:
        red()
        print("\nEligio: 4 -> Acelerar el arranque del sistema operativo\n")
        grub_faster()
    elif option == 5:
        print("\nEligio: 5 -> Instalar Todo\n")
        requirements()
        bspwm()
        grub_faster
        polybar()
    elif option == 6:
        red()
        print("\nEligio: 6 -> Salir\n")
        exit()
    elif option == 7:
        red()
        print("\nEligio: 7 -> Seleccionar Sistema Operativo\n")
        PrintOS()

    else:
        os.system("clear")
        red() 
        print("\nPor favor elija una opción del 1 al 7\n")
        while option != 1 or 2 or 3 or 4 or 5 or 6 or 7:
            menu()
def requirements():
    green()
    print("[+] Instalando requerimientos...\n")

    # Instalando Requerimientos
    os.system("sudo apt update")
    os.system("sudo apt install net-tools libuv1-dev build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y")
    os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y")
    os.system("sudo apt install bspwm rofi caja feh gnome-terminal scrot neovim xclip tmux acpi scrub bat wmname firejail rofi feh ranger -y")

    print("[+] Requerimientos instalados correctamente")

def bspwm ():
    
    green()
    print("[+] Instalando bspwm...\n")

    # Instalando los requeremientos necesarios
    os.system("sudo apt update")
    os.system("sudo apt install build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev ")
    # Instalando bspwm 
    os.system("git clone https://github.com/baskerville/bspwm.git")
    os.system("cd bspwm")
    os.system("make")
    os.system("sudo make install")
    os.system("sudo apt install bspwm")
    os.system("cd ..")
    # Eliminando el repositorio local de bspwm
    os.system("sudo rm -r bspwm")

    # Instalando sxhkd
    os.system("git clone https://github.com/baskerville/sxhkd.git")
    os.system("cd sxhkd")
    os.system("make")
    os.system("sudo make install")
    # Crea las carpetas de bspwm y sxhkd en ~/.config
    os.system("mkdir ~/.config/bspwm")
    os.system("mkdir ~/.config/sxhkd")
    os.system("cp examples/bspwmrc ~/.config/bspwm/")
    # Les da permisos de ejecucion a bspwmrc
    os.system("chmod +x ~/.config/bspwm/bspwmrc")
    os.system("cp ../sxhkdrc ~/.config/sxhkd/")
    # Eliminando el repositorio local de sxhkd
    os.system("sudo rm -r sxhkd")

    #Copiando`+
    #  el archivo bspwm_resize
    os.system("mkdir ~/.config/bspwm/scripts/")
    os.system("cp bspwm_resize ~/.config/bspwm/scripts/")
    os.system("chmod +x ~/.config/bspwm/scripts/bspwm_resize")
    
    print("\n[+] Bspwm instalado correctamente!")

def grub_faster():
    green()
    print("[+] ACELERANDO ARRANQUE...\n")

    os.system("sudo sed -i 's/GRUB_TIMEOUT=5/GRUB_TIMEOUT=0/' /etc/default/grub")
    os.system("sudo update-grub")
    time.sleep(2)
    print("\n[+] ARRANQUE ACELERADO!!!")

def polybar():

    green()   
    print("[+] Instalando polybar, picom, rofi ...\n")

    # Instalando los requerimientos necesarios
    os.system("sudo apt update")
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y")
    os.system("sudo apt update && sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev dunst firejail rofi feh ranger -y")
    # Instalando polybar
    os.system("git clone --recursive https://github.com/polybar/polybar")
    os.system("cd polybar")
    os.system("mkdir build")
    os.system("cd build")
    os.system("cmake ..")
    os.system("make -j$(nproc)")
    os.system("sudo make install")

    # Eliminando el repositorio local de polybar
    os.system("cd ../../ && sudo rm -r polybar")
 
    # Instalando picom
    os.system("git clone https://github.com/ibhagwan/picom.git")
    os.system("cd picom")
    os.system("git submodule update --init --recursive")
    os.system("meson --buildtype=release . build")
    os.system("ninja -C build")
    os.system("sudo ninja -C build install")

    # Eliminando el repositorio local de picom
    os.system("cd .. && sudo rm -r picom")
    
    # Añade el wallpaper
    os.system("mkdir ~/.wallpapers")
    os.system("cp wallpaper.jpg ~/.wallpapers")
    os.system("echo 'feh --bg-fill ~/.wallpapers/wallpaper.jpg' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'xsetroot -cursor_name left_ptr &' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'wmname LG3D &' >> ~/.config/bspwm/bspwmrc")

    # Instalando el tema de blue-sky modificado
    os.system("git clone https://github.com/VaughnValle/blue-sky.git")
    os.system("mkdir ~/.config/polybar")
    os.system("cd blue-sky/polybar/")
    os.system("cp * -r ~/.config/polybar/")
    os.system("echo '~/.config/polybar/./launch.sh' >> ~/.config/bspwm/bspwmrc ")
    os.system("cd fonts")
    os.system("sudo cp * /usr/share/fonts/truetype/")
    os.system("fc-cache -v")
    os.system("cd ../../../ ")
    
    # Copiando la config de rofi personalizada                 
    os.system("mkdir ~/.config/rofi")                       
    os.system("mkdir ~/.config/rofi/themes")                
    os.system("cp blue-sky/nord.rasi ~/.config/rofi/themes")

    #Eliminando el repositorio local de blue-sky y configurando la polybar 

    os.system("rm -r blue-sky")
    os.system("cd ~/.config/polybar/")
    os.system("rm current.ini workspace.ini")
    os.system("cd -")
    os.system("cp current.ini workspace.ini ~/.config/polybar/")
    os.system("mkdir ~/.config/bin")
    os.system("cp ethernet_status.sh hackthebox_status.sh target_to_hack.sh ~/.config/bin/")
    os.system("echo '' > ~/.config/bin/target")
 
    #Editando el archivo ~/.config/polybar/launch.sh

    os.system("echo 'polybar terciary -c ~/.config/polybar/current.ini &' >> ~/.config/polybar/launch.sh")
    os.system("echo 'polybar quaternary -c ~/.config/polybar/current.ini &' >> ~/.config/polybar/launch.sh")
    os.system("echo 'polybar quinary -c ~/.config/polybar/current.ini &' >> ~/.config/polybar/launch.sh")
    os.system("sed -i 's/polybar top -c ~/.config/polybar/current.ini &/#polybar top -c ~/.config/polybar/current.ini &/' ~/.config/polybar/launch.sh")
    os.system("sed -i 's/polybar primary -c ~/.config/polybar/current.ini &/#polybar primary -c ~/.config/polybar/current.ini &/' ~/.config/polybar/launch.sh")

    # Copiando los scripts settarget y cleartarget a /bin
    os.system("sudo settarget /bin")
    os.system("sudo cleartarget /bin")
    os.system("sudo chmod +x /bin/settarget")
    os.system("sudo chmod +x /bin/cleartarget")
   
    #Instalando la hacknerd font
    os.system("sudo cp Hack.zip /usr/local/share/fonts/")
    os.system("sudo unzip Hack.zip")
    os.system("sudo rm Hack.zip")
    os.system("fc-cache -v")

    #Cambiando el grupo de /opt/de root a usuario

    os.system("whoami>user.txt")
    os.system("user=$(cat user.txt)")
    os.system("groups yue>group.txt")
    os.system("group=$(awk '{print$1}' group.txt)")
    os.system("sudo chown $user:$group /opt/")

    #instalando Firefox

    os.system("sudo cp firefox.tar.bz2 /opt/")
    os.system("tar -xf firefox.tar.bz2")
    os.system("rm firefox.tar.bz2")

    # Copiando la config de picom
    os.system("mkdir ~/.config/picom")
    os.system("echo 'bspc config focus_follows_pointer true' >> ~/.config/bspwm/bspwmrc")
    
    expback = input("\nDesea usar los experimental-backends en picom? Si no se activa se puede detectar lentitud en el equipo al no disponer de una buena GPU. ¿Si o No? -> ")

    if expback == "si or Si or SI or sI":
        os.system("cp picom.conf ~/.config/picom")

    if expback == "no or No NO nO":
        os.system("cp picom-blur.conf ~/.config/picom/picom.conf")

    os.system("echo 'bspc config border_width 0' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'picom --experimental-backends &' >> ~/.config/bspwm/bspwmrc")

    # Instalando powerlevel10k para usuario
    os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k")
    os.system("echo 'source ~/.powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc")

    # Instalando powerlevel10k para root
    os.system("sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/.powerlevel10k")
    os.system("sudo echo 'source ~/.powerlevel10k/powerlevel10k.zsh-theme' >> /root/.zshrc")
   
    # Seleccionando si quiere configurar la p10k a su gusto o si quiere una identica a la de S4vitar
    optzsh=input("'\033[1;31m'\n¿Desea tener su zsh identica a la de s4vitar o desea ejecutar el asistente de instalacion de p10k?\nDigite Si para tener su zsh igual a la de S4vitar digite No para ejecutar el asistente")
    if optzsh == Si or si or sI or SI:
        os.system("cp ~.p10k.zsh")
        os.system("sudo cp ~.p10k.zsh")

    else:
        os.system("zsh")
    
    # Configurando como tipo de shell principal ls zsh para usuario
    os.system("chsh -s /usr/bin/zsh")

    # Configurando como tipo de shell principal ls zsh para root
    os.system("sudo chsh -s /usr/bin/zsh")

    # Para evitar un pequeño problema de permisos a la hora de desde el usuario root migrar con 'su' al usuario con bajos privilegios, ejecutamos los siguientes comandos:
    os.system("chown $user:$group /root")
    os.system("chown $user:$group /root/.cache -R")
    os.system("chown $user:$group /root/.local -R")
    
    # Creando enlace simbolico de root a usuario
    os.system("sudo cd /root/ && sudo ln -s -f ~/.zshrc .zshrc")
    os.system("cd -")

    # Quitando el pequeño saludo que sale al iniciar zsh
    os.system("""sudo sed -i 's/echo "Welcome to Parrot OS"/#echo "Welcome to Parrot OS"/' ~/.zshrc""")

    # Reparando el error que tira BurpSuite al inicio sobre java
    os.system("echo'# Fix the Java Problem' >> ~/.zshrc")
    os.system("echo'export _JAVA_AWT_WM_NONREPARENTING=1' >> ~/.zshrc")

    # configurando para que se pueda eliminar el historico de la zsh
    #os.system("sed -i's/setopt appendhistory")
    
############################################    # Añadiendo scripts personaliados de s4vitar. extractPorts, whichSystem...
    # Instalando bat
    os.system("sudo dpkg -i bat_0.18.3_amd64.deb")
    os.system("echo'# Custom Aliases' >> ~/.zshrc")
    os.system("""echo"alias cat='/bin/bat'" >> ~/.zshrc""")
    os.system("""echo"alias catn='/bin/cat'" >> ~/.zshrc""")
    os.system("""echo"alias catnl='/bin/bat --paging=never'" >> ~/.zshrc""")

    # Instalando lsd
    os.system("sudo dpkg -i lsd-musl_0.20.1_amd64.deb")
    os.system("""echo"alias ll='lsd -lh --group-dirs=first'" >> ~/.zshrc""")
    os.system("""echo"alias la='lsd -a --group-dirs=first'" >> ~/.zshrc""")
    os.system("""echo"alias l='lsd --group-dirs=first'" >> ~/.zshrc""")
    os.system("""echo"alias lla='lsd -lha --group-dirs=first'" >> ~/.zshrc""")
    os.system("""echo"alias ls='lsd --group-dirs=first'" >> ~/.zshrc""")

    # Instalando fzf
    os.system("git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf")
    os.system("~/.fzf/install --all")

    # Instalando sudo plugin para zsh
    os.system("sudo mkdir -p /usr/share/zsh-plugins/")
    os.system("chown $user:$group zsh-plugins")
    os.system("cd /usr/share/zsh-plugins/")
    os.system("wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/sudo/sudo.plugin.zsh")
    os.system("cd -")
    os.system("echo'source /usr/share/zsh-plugins/sudo.plugin.zsh >> ~/.zshrc")

    # Instalando tema nord para nvim en usuario 
    os.system("wget https://github.com/arcticicestudio/nord-vim/archive/master.zip")
    os.system("unzip master.zip")
    os.system("mkdir ~/.config/nvim")
    os.system("mv nord-vim-master/colors/ ~/.config/nvim")
    os.system("sudo rm -r nord-vim-master/")
    os.system("wget https://raw.githubusercontent.com/Necros1s/lotus/master/lotus.vim")
    os.system("wget https://raw.githubusercontent.com/Necros1s/lotus/master/lotusbar.vim")
    os.system("wget https://raw.githubusercontent.com/Necros1s/lotus/master/init.vim")
    os.system("mv *.vim ~/.config/nvim")
    os.system("echo 'colorscheme nord' >> ~/.config/nvim/init.vim")
    os.system("echo 'syntax on' >> ~/.config/nvim/init.vim")

    # Instalando tema nord para nvim en root
    os.system("wget https://github.com/arcticicestudio/nord-vim/archive/master.zip")
    os.system("unzip master.zip")
    os.system("rm master.zip")
    os.system("sudo mkdir /root/.config/nvim")
    os.system("sudo mv nord-vim-master/colors/ /root/.config/nvim")
    os.system("sudo rm -r nord-vim-master/")
    os.system("wget https://raw.githubusercontent.com/Necros1s/lotus/master/lotus.vim")
    os.system("wget https://raw.githubusercontent.com/Necros1s/lotus/master/lotusbar.vim")
    os.system("wget https://raw.githubusercontent.com/Necros1s/lotus/master/init.vim")
    os.system("sudo mv *.vim /root/.config/nvim")
    os.system("echo 'colorscheme nord' >> /root/.config/nvim/init.vim")
    os.system("echo 'syntax on' >> /root/.config/nvim/init.vim")

    # Instalando Oh My Tmux
    os.system("git clone https://github.com/gpakosz/.tmux.git /home/$USER/.tmux")
    os.system("ln -s -f .tmux/.tmux.conf /home/$USER")
    os.system("cp /home/$USER/.tmux/.tmux.conf.local /home/$USER")
    
    # Instalando Oh My Tmux para root
    os.system("sudo git clone https://github.com/gpakosz/.tmux.git /root/.tmux")
    os.system("sudo ln -s -f .tmux/.tmux.conf /root")
    os.system("sudo cp /root/.tmux/.tmux.conf.local /root")

    # Instalando wichSystem.py
    os.system("chmod +x wichSystem.py")
    os.system("sudo mv wichSystem.py /bin/")

    # Instalando fastTCPscan.go
    os.system("chmod +x fastTCPscan.go")
    os.system("sudo cp fastTCPscan.go /bin/")

    # Configurando el notify-send
    os.system("echo 'killall mate-notification-daemon; dunst &' >> ~/.config/bspwm/bspwmrc")

    #El usuario debera de elegir el tema rofi y presionar alt+a
    os.system("notify-send 'Atencion!!! rofi-theme-selector' 'Por favor seleccione el tema nord al final de la lista y luego presione la tecla enter para previsualizar el tema y luego presione las teclas alt + a'")
    os.system("rofi-theme-selector")

    print("\n[+] POLYBAR Y DEMAS INSTALADO!!!")

if __name__ == '__main__':
    menu()
