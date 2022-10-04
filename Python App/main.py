from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import colorama
import webbrowser

colorama.init()

screen_helper = """
ScreenManager:
    MenuScreen:
    StartScreen:
    LoginScreen:
    InfoScreen:
    NextScreen:
    AccountScreen:
    ClipboardScreen:
    TermuxScreen:
    PythonScreen:
    CScreen:
    CplusScreen:
    JavaScreen:
    HtmlScreen:
    ArdunioScreen:
    RustScreen:
    KotlinScreen:
    PerlScreen:
    GoScreen:
    PhpScreen:
    TermsScreen:
    AboutScreen:
    HelpScreen:

<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: 'WELCOME !'
        halign: 'center'
        font_style : 'H6'
    MDLabel:
        text: 'Press Start To Continue'
        pos_hint: {'center_x' :0.5, 'center_y' :0.45}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 136/255,136/255,136/255,1 
        font_style : 'Button'
    Image:
        source: "new logo.png"
        size_hint: 0.80,0.80
        pos_hint: {'center_x' :0.5, 'center_y' :0.75}
    Image:
        source: "images (2) (11).jpeg"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.82, 'center_y' :0.09}
    MDRaisedButton:
        text: 'Start'
        pos_hint:{'center_x' :0.5, 'center_y' :0.3}
        on_press: root.manager.current = 'Start'
<StartScreen>:
    name: 'Start'
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.2}
        font_style: 'Button'
        on_press: root.manager.current = 'menu'
    MDLabel:
        text: 'Login'
        font_style: 'H4'
        halign: 'center'
        pos_hint: {'center_x' :0.5, 'center_y' :0.8}
        theme_text_color: "Custom"
        text_color: 1,0,0,1
        size_hint: 0.7,1
    MDLabel:
        text: 'Username:'
        font_style: 'Button'
        halign : 'center'
        pos_hint: {'center_x' :0.35, 'center_y' :0.65}
        theme_text_color: "Custom"
        text_color: 0,0,0,1
    MDTextField:
        id:username
        hint_text: "Enter Username"
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        icon_right: "account-circle"
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        size_hint_x: None
        width: 200
    MDLabel:
        text: 'Password:'
        font_style: 'Button'
        halign : 'center'
        pos_hint: {'center_x' :0.35, 'center_y' :0.49}
        theme_text_color: "Custom"
        text_color: 0,0,0,1
    MDTextField:
        id:password
        hint_text: "Enter Password"
        pos_hint: {'center_x' :0.5, 'center_y' :0.42}
        icon_right: "lock"
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        size_hint_x: None
        width: 200
        password: True
    MDRaisedButton:
        text: 'Login'
        pos_hint:{'center_x' :0.5, 'center_y' :0.3}
        on_press:app.handle_login(root.manager,username,password)
    MDTextButton:
        text: 'Get Your Username And Password'
        pos_hint:{'center_x' :0.5, 'center_y' :0.1}
        font_style: 'Caption'
        theme_text_color: "Custom"
        text_color: 136/255,136/255,136/255,1 
        on_press: root.manager.current = 'info'
<InfoScreen>:
    name: 'info'
    MDLabel:
        text: 'Username : tech_machine'
        halign: 'center'
        font_style: 'Button'
    MDLabel:
        text: 'Password : 1234'
        halign: 'center'
        pos_hint: {'center_x' :0.5, 'center_y' :0.4}
        font_style: 'Button'   
    Image:
        source: "new logo.png"
        size_hint: 0.80,0.80
        pos_hint: {'center_x' :0.5, 'center_y' :0.75}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.2}
        font_style: 'Button'
        on_press: root.manager.current = 'Start'
<LoginScreen>:
    name: 'login'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            md_bg_color: app.theme_cls.accent_color
            md_bg_color: 0,0,0,1
    MDIconButton:
        icon: 'home'
        pos_hint:{'center_x' :0.08, 'center_y' :0.05}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        on_press: root.manager.current = 'login' 
    MDIconButton:
        icon: 'account'
        pos_hint:{'center_x' :0.9, 'center_y' :0.05} 
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1 
        on_press: root.manager.current = 'account' 
    MDIconButton:
        icon: 'clipboard-text-outline'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05} 
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        on_press: root.manager.current = 'clipboard'
    Image:
        source: "tumblr_0d721771474a58bed4f508d1b35e17dd_e71a1cf6_540.gif"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.7}
    MDRaisedButton:
        text: 'Next'
        pos_hint:{'center_x' :0.5, 'center_y' :0.15}
        font_style: 'Button'
        on_press: root.manager.current = 'next'     
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.2, 'center_y' :0.87}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'termux'
        Image:
            source: "TERMUX.png"
            size_hint: 1,2
            pos_hint: {'center_x' :0.2, 'center_y' :0.87}
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.8, 'center_y' :0.87}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'python'
        Image:
            source: "PYTHON.jpeg"
            size_hint: 1,2
            pos_hint: {'center_x' :0.8, 'center_y' :0.87}   
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.2, 'center_y' :0.63}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'c'
        Image:
            source: "C.png"
            size_hint: 1,2
            pos_hint: {'center_x' :0.2, 'center_y' :0.63}
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.8, 'center_y' :0.63}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'c++'
        Image:
            source: "C++.jpeg"
            size_hint: 1,2
            pos_hint: {'center_x' :0.8, 'center_y' :0.63}
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.2, 'center_y' :0.39}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'java'
        Image:
            source: "JAVA.jpeg"
            size_hint: 1,2
            pos_hint: {'center_x' :0.2, 'center_y' :0.39}
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.8, 'center_y' :0.39}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'html'
        Image:
            source: "HTML.jpeg"
            size_hint: 1,2
            pos_hint: {'center_x' :0.8, 'center_y' :0.39}
<NextScreen>:
    name: 'next'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            md_bg_color: app.theme_cls.accent_color
            md_bg_color: 0,0,0,1
    MDIconButton:
        icon: 'home'
        pos_hint:{'center_x' :0.08, 'center_y' :0.05}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        on_press: root.manager.current = 'login' 
    MDIconButton:
        icon: 'account'
        pos_hint:{'center_x' :0.9, 'center_y' :0.05} 
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1 
        on_press: root.manager.current = 'account' 
    MDIconButton:
        icon: 'clipboard-text-outline'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05} 
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        on_press: root.manager.current = 'clipboard'
    Image:
        source: "tumblr_0d721771474a58bed4f508d1b35e17dd_e71a1cf6_540.gif"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {'center_x' :0.5, 'center_y' :0.7}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.15}
        font_style: 'Button'
        on_press: root.manager.current = 'login'
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.2, 'center_y' :0.87}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'ardunio'
        Image:
            source: "Ardunio.png"
            size_hint: 1,2
            pos_hint: {'center_x' :0.2, 'center_y' :0.87}
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.8, 'center_y' :0.87}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'rust'
        Image:
            source: "Rust.jpg"
            size_hint: 1,2
            pos_hint: {'center_x' :0.8, 'center_y' :0.87}   
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.2, 'center_y' :0.63}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'kotlin'
        Image:
            source: "Kotlin.png"
            size_hint: 1,2
            pos_hint: {'center_x' :0.2, 'center_y' :0.63}
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.8, 'center_y' :0.63}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'perl'
        Image:
            source: "Perl.jpeg"
            size_hint: 1,2
            pos_hint: {'center_x' :0.8, 'center_y' :0.63}
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.2, 'center_y' :0.39}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'go'
        Image:
            source: "Go.jpeg"
            size_hint: 1,2
            pos_hint: {'center_x' :0.2, 'center_y' :0.39}
    MDRaisedButton:
        md_bg_color: 0,0,0,1
        pos_hint:{'center_x' :0.8, 'center_y' :0.39}
        font_style: 'Button'
        size_hint: 0.3,0.2
        on_press: root.manager.current = 'php'
        Image:
            source: "PHP.jpeg"
            size_hint: 1,2
            pos_hint: {'center_x' :0.8, 'center_y' :0.39} 
<AccountScreen>:
    name: 'account'
    Image:
        source: "new logo.png"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.82}
    MDLabel:
        text: 'TECH_MACHINE'
        halign: 'center'
        bold: True
        font_style : 'Button'
        pos_hint: {'center_x' :0.5, 'center_y' :0.63}
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            md_bg_color: app.theme_cls.accent_color
            md_bg_color: 0,0,0,1
    MDRaisedButton:
        text: 'Terms And Condition'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.55}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_press: root.manager.current = 'terms' 
    MDRaisedButton:
        text: 'Follow Us'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.44}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_press: root.manager.current = 'about' 
    MDRaisedButton:
        text: 'Help'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.33}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_press: root.manager.current = 'help'
    MDRaisedButton:
        text: 'LogOut'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_press: root.manager.current = 'Start'
    MDIconButton:
        icon: 'home'
        pos_hint:{'center_x' :0.08, 'center_y' :0.05}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        on_press: root.manager.current = 'login' 
    MDIconButton:
        icon: 'account'
        pos_hint:{'center_x' :0.9, 'center_y' :0.05} 
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1 
        on_press: root.manager.current = 'account' 
    MDIconButton:
        icon: 'clipboard-text-outline'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05} 
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        on_press: root.manager.current = 'clipboard'
<ClipboardScreen>
    name: 'clipboard'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar: 
            md_bg_color: app.theme_cls.accent_color
            md_bg_color: 0,0,0,1
    MDIconButton:
        icon: 'home'
        pos_hint:{'center_x' :0.08, 'center_y' :0.05}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        on_press: root.manager.current = 'login' 
    MDIconButton:
        icon: 'account'
        pos_hint:{'center_x' :0.9, 'center_y' :0.05} 
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1 
        on_press: root.manager.current = 'account' 
    MDIconButton:
        icon: 'clipboard-text-outline'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05} 
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        on_press: root.manager.current = 'clipboard'
    MDLabel:
        text: 'COURSE'
        halign: 'center'
        font_style : 'H6'
        pos_hint: {'center_x' :0.5, 'center_y' :0.98} 
        theme_text_color: "Custom"
        text_color: 1,0,0,1
    MDRaisedButton:
        text: 'Termux'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.92}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'termux'
    MDRaisedButton:
        text: 'Python'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.85}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'python'
    MDRaisedButton:
        text: 'C'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.78}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'c'
    MDRaisedButton:
        text: 'C++'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.71}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'c++'
    MDRaisedButton:
        text: 'Java'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.64}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'java'
    MDRaisedButton:
        text: 'HTML'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.57}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'html'
    MDRaisedButton:
        text: 'Arduino'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'ardunio'
    MDRaisedButton:
        text: 'Rust'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.43}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'rust'
    MDRaisedButton:
        text: 'Kotlin'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.36}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'kotlin'
    MDRaisedButton:
        text: 'Perl'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.29}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'perl'
    MDRaisedButton:
        text: 'Go'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'go'
    MDRaisedButton:
        text: 'PHP'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.15}
        size_hint: 1,0.05
        line_color: 0,0,0,1
        on_press: root.manager.current = 'php'
<TermuxScreen>:
    name: 'termux'
    Image:
        source: "TERMUX.png"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'login'
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(0)
    MDRaisedButton:
        text: 'Different Commands'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(1)
    MDRaisedButton:
        text: 'Hacking Tools'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(2)
<PythonScreen>:
    name: 'python'
    Image:
        source: "PYTHON.jpeg"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'login'
    MDRaisedButton:
        text: 'History Of Python'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(3)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(4)
    MDRaisedButton:
        text: 'Basics Of Python'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(5)
    MDRaisedButton:
        text: 'Different Applications Of Python'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(6)
<CScreen>:
    name: 'c'
    Image:
        source: "C.png"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'login'
    MDRaisedButton:
        text: 'History Of C'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(7)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(8)
    MDRaisedButton:
        text: 'Basics Of C'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(9)
    MDRaisedButton:
        text: 'Different Applications Of C'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(10)
<CplusScreen>:
    name: 'c++'
    Image:
        source: "C++.jpeg"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'login'
    MDRaisedButton:
        text: 'History Of C++'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(11)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(12)
    MDRaisedButton:
        text: 'Basics Of C++'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(13)
    MDRaisedButton:
        text: 'Different Applications Of C++'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(14)
<JavaScreen>:
    name: 'java'
    Image:
        source: "JAVA.jpeg"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'login'
    MDRaisedButton:
        text: 'History Of JAVA'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(15)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(16)
    MDRaisedButton:
        text: 'Basics Of JAVA'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(17)
    MDRaisedButton:
        text: 'Different Applications Of JAVA'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(18)
<HtmlScreen>:
    name: 'html'
    Image:
        source: "HTML.jpeg"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'login'
    MDRaisedButton:
        text: 'History Of HTML'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(19)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(20)
    MDRaisedButton:
        text: 'Basics Of HTML'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(21)
    MDRaisedButton:
        text: 'Different Applications Of HTML'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(22)
<ArdunioScreen>:
    name: 'ardunio'
    Image:
        source: "Ardunio.png"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'next'
    MDRaisedButton:
        text: 'History Of Arduino'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(23)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(24)
    MDRaisedButton:
        text: 'Basics Of Arduino'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(25)
    MDRaisedButton:
        text: 'Different Applications Of Arduino'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(26)
<RustScreen>:
    name: 'rust'
    Image:
        source: "Rust.jpg"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'next'
    MDRaisedButton:
        text: 'History Of Rust'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(27)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(28)
    MDRaisedButton:
        text: 'Basics Of Rust'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(29)
    MDRaisedButton:
        text: 'Different Applications Of Rust'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(30)
<KotlinScreen>:
    name: 'kotlin'
    Image:
        source: "Kotlin.png"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'next'
    MDRaisedButton:
        text: 'History Of Kotlin'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(31)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(32)
    MDRaisedButton:
        text: 'Basics Of Kotlin'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(33)
    MDRaisedButton:
        text: 'Different Applications Of Kotlin'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(34)
<PerlScreen>:
    name: 'perl'
    Image:
        source: "Perl.jpeg"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'next'
    MDRaisedButton:
        text: 'History Of Perl'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(35)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(36)
    MDRaisedButton:
        text: 'Basics Of Perl'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(37)
    MDRaisedButton:
        text: 'Different Applications Of Perl'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(38)
<GoScreen>:
    name: 'go'
    Image:
        source: "Go.jpeg"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'next'
    MDRaisedButton:
        text: 'History Of GO'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(39)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(40)
    MDRaisedButton:
        text: 'Basics Of GO'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(41)
    MDRaisedButton:
        text: 'Different Applications Of GO'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(42)
<PhpScreen>:
    name: 'php'
    Image:
        source: "PHP.jpeg"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.86}
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'next'
    MDRaisedButton:
        text: 'History Of PHP'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.58}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(43)
    MDRaisedButton:
        text: 'Introduction'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.46}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(44)
    MDRaisedButton:
        text: 'Basics Of PHP'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.34}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(45)
    MDRaisedButton:
        text: 'Different Applications Of PHP'
        md_bg_color: [44/255,45/255,47/255,1]
        pos_hint: {'center_x' :0.5, 'center_y' :0.22}
        size_hint: 1,0.09
        line_color: 0,0,0,1
        on_release: app.launch_link(46)
<TermsScreen>
    name: 'terms'
    MDLabel:
        text: 'TERMS AND CONDITIONS'
        pos_hint: {'center_x' :0.5, 'center_y' :0.95}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'H6'
    MDLabel:
        text: 'WELCOME! First of all we are not responsible for any misuse of any information. The information is only for educational purpose. You can contact through my e-mail for any help, unwanted e-mails are not acceptable. This application will not access user storage, data, files, photos. The user need not login through his name, the name and password is already given so that user need not revel their identity. User are not allowed to modify or make any changes in application. No guide is requried to use this application, user friendly etc. User are not allowed to violate the rules, if rules are violated that user is not allowed to use this app again. If yes click and continue.'
        pos_hint: {'center_x' :0.5, 'center_y' :0.75}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Body2'
    MDCheckbox:
        pos_hint: {'center_x' :0.23, 'center_y' :0.51}
        on_press: root.manager.current = 'login'
    MDLabel:
        text: 'i agree to terms and conditions'
        pos_hint: {'center_x' :0.5, 'center_y' :0.55}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
    MDLabel:
        text: '"To continue click the box"'
        pos_hint: {'center_x' :0.51, 'center_y' :0.51}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 136/255,136/255,136/255,1
        font_style : 'Body2'
    Image:
        source: "new logo.png"
        size_hint: 0.70,0.70
        pos_hint: {'center_x' :0.5, 'center_y' :0.3}
<AboutScreen>
    name: 'about'
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'account'   
    MDIconButton:
        icon: 'github'
        pos_hint:{'center_x' :0.25, 'center_y' :0.85}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        user_font_size: "110sp"
        md_bg_color: 0,0,0,1
        on_release: app.launch_link(47)
    MDLabel:
        text: 'GitHub'
        pos_hint: {'center_x' :0.25, 'center_y' :0.72}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
    MDIconButton:
        icon: 'web'
        pos_hint:{'center_x' :0.75, 'center_y' :0.85}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        user_font_size: "110sp"
        md_bg_color: 0,0,0,1
        on_release: app.launch_link(48)
    MDLabel:
        text: 'WEBSITE'
        pos_hint: {'center_x' :0.75, 'center_y' :0.72}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
    MDIconButton:
        icon: 'youtube'
        pos_hint:{'center_x' :0.25, 'center_y' :0.58}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        user_font_size: "110sp"
        md_bg_color: 0,0,0,1
        on_release: app.launch_link(49)
    MDLabel:
        text: 'youtube'
        pos_hint: {'center_x' :0.25, 'center_y' :0.45}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
    MDIconButton:
        icon: 'gmail'
        pos_hint:{'center_x' :0.75, 'center_y' :0.58}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        user_font_size: "110sp"
        md_bg_color: 0,0,0,1
        on_release: app.launch_link(50)
    MDLabel:
        text: 'g-mail'
        pos_hint: {'center_x' :0.75, 'center_y' :0.45}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
    MDLabel:
        text: 'TECH_MACHINE'
        pos_hint: {'center_x' :0.5, 'center_y' :0.28}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
<HelpScreen>:
    name: 'help'
    MDRaisedButton:
        text: 'Back'
        pos_hint:{'center_x' :0.5, 'center_y' :0.05}
        on_press: root.manager.current = 'account' 
    MDIconButton:
        icon: 'gmail'
        pos_hint:{'center_x' :0.5, 'center_y' :0.65}
        theme_text_color: 'Custom'
        text_color: app.theme_cls.accent_color
        text_color: 1,1,1,1
        user_font_size: "100sp"
        md_bg_color: 0,0,0,1
        on_release: app.launch_link(50)
    MDLabel:
        text: 'For Any Help Contact Through My G-Mail'
        pos_hint: {'center_x' :0.5, 'center_y' :0.8}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'H6'
    MDLabel:
        text: 'TECH_MACHINE'
        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
    MDLabel:
        text: 'NOTE  :  The Content In This App Is Only For Educational Purposes Only. We Are Not Responsible For Any Misuse Of Information'
        pos_hint: {'center_x' :0.5, 'center_y' :0.4}
        halign:'center'
        theme_text_color: "Custom"
        text_color: 0,0,0,1
        font_style : 'Button'
"""


class MenuScreen(Screen):
    pass

class StartScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

class NextScreen(Screen):
    pass

class AccountScreen(Screen):
    pass

class ClipboardScreen(Screen):
    pass

class TermuxScreen(Screen):
    pass

class PythonScreen(Screen):
    pass

class CScreen(Screen):
    pass

class CplusScreen(Screen):
    pass

class JavaScreen(Screen):
    pass

class HtmlScreen(Screen):
    pass

class ArdunioScreen(Screen):
    pass

class RustScreen(Screen):
    pass

class KotlinScreen(Screen):
    pass

class PerlScreen(Screen):
    pass

class GoScreen(Screen):
    pass

class PhpScreen(Screen):
    pass

class TermsScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(MenuScreen(name='start'))
sm.add_widget(MenuScreen(name='login'))
sm.add_widget(MenuScreen(name='info'))
sm.add_widget(MenuScreen(name='next'))
sm.add_widget(MenuScreen(name='account'))
sm.add_widget(MenuScreen(name='clipboard'))
sm.add_widget(MenuScreen(name='termux'))
sm.add_widget(MenuScreen(name='python'))
sm.add_widget(MenuScreen(name='c'))
sm.add_widget(MenuScreen(name='c++'))
sm.add_widget(MenuScreen(name='java'))
sm.add_widget(MenuScreen(name='html'))
sm.add_widget(MenuScreen(name='ardunio'))
sm.add_widget(MenuScreen(name='rust'))
sm.add_widget(MenuScreen(name='kotlin'))
sm.add_widget(MenuScreen(name='perl'))
sm.add_widget(MenuScreen(name='go'))
sm.add_widget(MenuScreen(name='php'))
sm.add_widget(MenuScreen(name='terms'))
sm.add_widget(MenuScreen(name='about'))
sm.add_widget(MenuScreen(name='help'))

class Tech_MachineApp(MDApp):
    username = "TECH_MACHINE"
    password = "1234"

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.icon = "new logo.png"
        self.presplash = "Presplash.png"
        return screen

    def launch_link(self, index):
        link = ''
        if index == 0:
            link = 'https://drive.google.com/file/d/1-Mz5maCSo5TpQ6Mw8PaAahz9IuLqB680/view?usp=drivesdk'
        elif index == 1:
            link = 'https://drive.google.com/file/d/1-dYuGXrI4MmYMGUiM31EN_pFsHiRjmwU/view?usp=drivesdk'
        elif index == 2:
            link = 'https://drive.google.com/file/d/10LKfAT1x4hHWkC6J5wLGrHc5MEH6WO2N/view?usp=drivesdk'
        elif index == 3:
            link = 'https://drive.google.com/file/d/1wSwDF61ky6vfRTIZOYbSyd0QQwChp9cf/view?usp=drivesdk'
        elif index == 4:
            link = 'https://drive.google.com/file/d/1wTt0-lrV34TATopQQOQ234dJbOaYw9qY/view?usp=drivesdk'
        elif index == 5:
            link = 'https://drive.google.com/file/d/1wW3okNeUeba2gqQPIWrz75QZXCopNxc9/view?usp=drivesdk'
        elif index == 6:
            link = 'https://drive.google.com/file/d/1wYk57KSWO6U2TetHMxkNaVGPwPQPeVhS/view?usp=drivesdk'
        elif index == 7:
            link = 'https://drive.google.com/file/d/116SX8xNXrh3nbYUW0aTKU3HboGvp7kAN/view?usp=drivesdk'
        elif index == 8:
            link = 'https://drive.google.com/file/d/19hhmY8Nxq7RnZGw89M0wfAcLs1Ar8mvr/view?usp=drivesdk'
        elif index == 9:
            link = 'https://drive.google.com/file/d/11z61ZDjlx5RxaY0AyM1I5GEdU0zNyc4b/view?usp=drivesdk'
        elif index == 10:
            link = 'https://drive.google.com/file/d/19p7MyrmcCc4HuyZQd4azc7SwwpeX_0gV/view?usp=drivesdk'
        elif index == 11:
            link = 'https://drive.google.com/file/d/1AHDDVIDARCVRTs0PFgrFqxRc9Apbgy-B/view?usp=drivesdk'
        elif index == 12:
            link = 'https://drive.google.com/file/d/1APHLq_Xc8Io8TRjuuBpzoUzpJenONp9d/view?usp=drivesdk'
        elif index == 13:
            link = 'https://drive.google.com/file/d/1AWYn6PVvzFJq9-xK7WUF5tdUZqy2iuHW/view?usp=drivesdk'
        elif index == 14:
            link = 'https://drive.google.com/file/d/1AhxeRpkLThCZzIbAEWWjD7iUeBM9H2wH/view?usp=drivesdk'
        elif index == 15:
            link = 'https://drive.google.com/file/d/1a3tfyUXIptjBIo3qo1MIZudPw-6jgBLx/view?usp=drivesdk'
        elif index == 16:
            link = 'https://drive.google.com/file/d/1a7KdDmikIwijVCLmtG48Q29-p-ckh83P/view?usp=drivesdk'
        elif index == 17:
            link = 'https://drive.google.com/file/d/1_whPDF51gQIqe_CWyciPDNiS47FBGGI-/view?usp=drivesdk'
        elif index == 18:
            link = 'https://drive.google.com/file/d/1aBNvN11HJP9gkeWhLphxX6at1s0ZeX5N/view?usp=drivesdk'
        elif index == 19:
            link = 'https://drive.google.com/file/d/1q9alWi_dahhGNzkVIKY7OZ4EWXTRqcrD/view?usp=drivesdk'
        elif index == 20:
            link = 'https://drive.google.com/file/d/1qS-oT14MNE5vaDUUvqRNN6BR8qZUfqrk/view?usp=drivesdk'
        elif index == 21:
            link = 'https://drive.google.com/file/d/1qYkmq0Z5m6YpzuNGqJ_v5mL5wYzREc__/view?usp=drivesdk'
        elif index == 22:
            link = 'https://drive.google.com/file/d/1qg2Vyhl6E5dITwuxAqJKM3henjD3xtCx/view?usp=drivesdk'
        elif index == 23:
            link = 'https://drive.google.com/file/d/10S9fJCUuit-o3fTcHNOrcfzUFXWoBh9F/view?usp=drivesdk'
        elif index == 24:
            link = 'https://drive.google.com/file/d/10Snmg-D4_0q25Tsga97xZwJS-uuYbJ-F/view?usp=drivesdk'
        elif index == 25:
            link = 'https://drive.google.com/file/d/10U7Oi7PJNvOfB0TYw2h3NpxyVymIp-_9/view?usp=drivesdk'
        elif index == 26:
            link = 'https://drive.google.com/file/d/10ZmRwrkktjbha-R_lg6IpPatoblg9Q0Q/view?usp=drivesdk'
        elif index == 27:
            link = 'https://drive.google.com/file/d/15euthPa33mdklSNcEy8bBIB08sK-K2_X/view?usp=drivesdk'
        elif index == 28:
            link = 'https://drive.google.com/file/d/15ezVVmXflk9p4KCYon5ON1hbJFB2tIKv/view?usp=drivesdk'
        elif index == 29:
            link = 'https://drive.google.com/file/d/15iTYiA6SenO06h5SgTDjbbVWyls_R5Q8/view?usp=drivesdk'
        elif index == 30:
            link = 'https://drive.google.com/file/d/15jcmYX4i1LvtTUa4jX6pCyo9sP7njiIH/view?usp=drivesdk'
        elif index == 31:
            link = 'https://drive.google.com/file/d/14_iQePslzkRszSpu5bw4dAkjMN76cQyE/view?usp=drivesdk'
        elif index == 32:
            link = 'https://drive.google.com/file/d/14b7kgSEZ-obW5FVr2RSOB7EdhPXU9bIW/view?usp=drivesdk'
        elif index == 33:
            link = 'https://drive.google.com/file/d/14dRG1g5aq5MweY5psDNJiw4kkfGxsOK4/view?usp=drivesdk'
        elif index == 34:
            link = 'https://drive.google.com/file/d/14eKgeY98dqZxlhs9-eq3y7Is0yisaJO2/view?usp=drivesdk'
        elif index == 35:
            link = 'https://drive.google.com/file/d/13EzQRik_L6v8h--UD3ef7NW27MXs9GGp/view?usp=drivesdk'
        elif index == 36:
            link = 'https://drive.google.com/file/d/13F_ncnyBYUauLa321tLWxS-Sfi0TS9EW/view?usp=drivesdk'
        elif index == 37:
            link = 'https://drive.google.com/file/d/13bk10UONzp0NrIqx5lHEGo7U9rCBYbtS/view?usp=drivesdk'
        elif index == 38:
            link = 'https://drive.google.com/file/d/13ctK2sD1kCHngFRTWcAH9Yb37DwmrCZg/view?usp=drivesdk'
        elif index == 39:
            link = 'https://drive.google.com/file/d/12RnGoqrpsr05HfUX3kBnxbe1rM3GNaEA/view?usp=drivesdk'
        elif index == 40:
            link = 'https://drive.google.com/file/d/12SXlrcmnhJwLx88DM8Rd53w7tk6IgSgm/view?usp=drivesdk'
        elif index == 41:
            link = 'https://drive.google.com/file/d/12UzPujOJBJeDQpWqAOYYIBblTTEF1oEf/view?usp=drivesdk'
        elif index == 42:
            link = 'https://drive.google.com/file/d/12X1K0hCOUGoZr1CGYKozXoqZ_J8x6JDH/view?usp=drivesdk'
        elif index == 43:
            link = 'https://drive.google.com/file/d/15VYo5dFeIkR9u0wIGv-7cMJcydrmo7x8/view?usp=drivesdk'
        elif index == 44:
            link = 'https://drive.google.com/file/d/11BT0KcPEo5HZvoQNrGTA44VGbNyuM5FO/view?usp=drivesdk'
        elif index == 45:
            link = 'https://drive.google.com/file/d/15X2xPhj00Jgxd4FJMMNZCbJ_KjoEKVFA/view?usp=drivesdk'
        elif index == 46:
            link = 'https://drive.google.com/file/d/15ajAYjDZMtoZzy7fWfCjvFs4DudTaU-b/view?usp=drivesdk'
        elif index == 47:
            link = 'https://github.com/Krupal-create'
        elif index == 48:
            link = 'techmachine.data.blog'
        elif index == 49:
            link = 'https://youtube.com/channel/UCtinUWWfayuaGKuTEHHTkIQ'
        elif index == 50:
            link = 'techmachine13@gmail.com'
        webbrowser.open(link)

    def handle_login(self, screen_manager, username, password):

        if username.text == self.username and password.text == self.password:
            print(colorama.Fore.GREEN + f"Logged in successfully as {self.username}")
            colorama.reinit()
            screen_manager.current = "terms"

        else:
            print(colorama.Fore.RED + "INVALID CREDENTIALS, TRY AGAIN !!!")
            colorama.reinit()

        username.text = ""
        password.text = ""

Tech_MachineApp().run()