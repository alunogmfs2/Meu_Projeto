import customtkinter


def abrir_fechar(abrir, fechar):
    fechar.destroy()
    abrir.mainloop()


bem_vindo = customtkinter.CTk()

lj = bem_vindo.winfo_screenwidth() # type: ignore # Largura da Janela
aj = bem_vindo.winfo_screenheight() # type: ignore # Altura da Janela

largura = 800
altura = 600

x = (lj / 2) - (largura / 2)
y = (aj / 2) - (altura / 2) # Centraliza a Janela na Tela

janela = f"{largura}x{altura}+{int(x)}+{int(y)}"


def bem_vindo_f():
    bem_vindo.title('Bem Vindo')
    bem_vindo.geometry(janela) # Tamanho e Posicao da Janela

    tbem_vindo = customtkinter.CTkLabel(bem_vindo, text='Bem vindo ao <nome do app>', fg_color='transparent', font=('Arial', 36))
    bcontinuar = customtkinter.CTkButton(bem_vindo, text='Continuar', command=modos_f)

    tbem_vindo.pack(pady=180)
    bcontinuar.pack()


def modos_f():
    global bem_vindo
    modos = customtkinter.CTk()
    modos.title('Modos')
    modos.geometry(janela)

    tsmodos = customtkinter.CTkLabel(modos, text='Selecione a seu Rotina atual:', fg_color='transparent', font=('Arial', 32))
    tsmodos.pack(pady=10)
    abrir_fechar(modos, bem_vindo)
    

bem_vindo_f()

if __name__ == '__main__':
    bem_vindo.mainloop()
