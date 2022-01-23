import dearpygui.dearpygui as dpg
from controllers.master import *

def master_window():
    with dpg.window(label="Mestre",width=600, no_close=True, pos=(0, 0)):
        with dpg.tab_bar(label="MenuMaster"):
            with dpg.tab(label="Geral"):
                with dpg.group():
                    dpg.add_text("Nome da Campanha")
                    dpg.add_input_text(width=450, tag="campanha_nome")
                    dpg.add_text("Campanha")
                    dpg.add_input_text(width=450, multiline=True, tag="campanha")
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                with dpg.group():
                    dpg.add_text("Tabela de Dificuldades")
                    with dpg.table(label="Difficulties", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Teste", width=125, width_fixed=True)
                        dpg.add_table_column(label="Descrição")
                        
                        with dpg.table_row():
                            dpg.add_text("Força")
                            dpg.add_text("Combate corpo-a-corpo, peso, escalar, nadar")
                        
                        with dpg.table_row():
                            dpg.add_text("Resis. Física")
                            dpg.add_text("Resistir a danos físicos, se defender")
                        
                        with dpg.table_row():
                            dpg.add_text("Resis. Mental")
                            dpg.add_text("Resistir qualquer ação que afete a mente")
                        
                        with dpg.table_row():
                            dpg.add_text("Sobrevivência")
                            dpg.add_text("Resistir elementos naturais, venenos ou químicas")
                        
                        with dpg.table_row():
                            dpg.add_text("Agilidade")
                            dpg.add_text("Iniciativa de combate, armas de curta, média e longa distância e arremessar objetos")
                        
                        with dpg.table_row():
                            dpg.add_text("Destreza")
                            dpg.add_text("Performaces corporais, esportes e conduzir veículos")
                        
                        with dpg.table_row():
                            dpg.add_text("Competência")
                            dpg.add_text("Realizar um trabalho específico (decifrar um código, destrancar uma porta)")
                        
                        with dpg.table_row():
                            dpg.add_text("Criatividade")
                            dpg.add_text("Imaginar, deduzir, investigar, rastrear, analisar, improvisar objetos ou situações")
                        
                        with dpg.table_row():
                            dpg.add_text("Manipulação")
                            dpg.add_text("Blefar, trapacear, influenciar, simular, atuar e liderar")
                        
                        with dpg.table_row():
                            dpg.add_text("Sorte")
                            dpg.add_text("Qualquer ação que não dependa da sua performance")
                    
                    dpg.add_spacer()
                    dpg.add_text("Exemplos de ações genéricas")
                    with dpg.table(label="Example", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Ação")
                        dpg.add_table_column(label="Dificuldade")
                        dpg.add_table_column(label="Teste")

                        with dpg.table_row():
                            dpg.add_text("Saltar 1,5 metros")
                            dpg.add_text("20")
                            dpg.add_text("Força")

                        with dpg.table_row():
                            dpg.add_text("Esquivar de um golpe")
                            dpg.add_text("21")
                            dpg.add_text("Agilidade")

                        with dpg.table_row():
                            dpg.add_text("Intimidar")
                            dpg.add_text("22")
                            dpg.add_text("Manipulação")

                        with dpg.table_row():
                            dpg.add_text("Identificar blefe")
                            dpg.add_text("26")
                            dpg.add_text("Resis. Mental")

                        with dpg.table_row():
                            dpg.add_text("Ganhar no cara e coroa")
                            dpg.add_text("31")
                            dpg.add_text("Sorte")

                        with dpg.table_row():
                            dpg.add_text("Salto carpado")
                            dpg.add_text("38")
                            dpg.add_text("Destreza")

                        with dpg.table_row():
                            dpg.add_text("Pintar um retrato")
                            dpg.add_text("41")
                            dpg.add_text("Criatividade")

                        with dpg.table_row():
                            dpg.add_text("Resistir um golpe")
                            dpg.add_text("42")
                            dpg.add_text("Resis. Física")

                        with dpg.table_row():
                            dpg.add_text("Resistir hipotermia")
                            dpg.add_text("42")
                            dpg.add_text("Sobrevivência")

                        with dpg.table_row():
                            dpg.add_text("Falsificar documento")
                            dpg.add_text("52")
                            dpg.add_text("Competência")

                    dpg.add_spacer()
                    dpg.add_text("Estados")
                    with dpg.table(label="States", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Estado")
                        dpg.add_table_column(label="Testes afetados (-)")

                        with dpg.table_row():
                            dpg.add_text("Medo")
                            dpg.add_text("Resis. Mental, Competência")

                        with dpg.table_row():
                            dpg.add_text("Desespero")
                            dpg.add_text("Resis. Mental, Competência, Destreza")

                        with dpg.table_row():
                            dpg.add_text("Estresse")
                            dpg.add_text("Resis. Mental, Criatividade, Manipulação")

                        with dpg.table_row():
                            dpg.add_text("Descontrole")
                            dpg.add_text("Resis. Mental, Criatividade, Manipulação")

                        with dpg.table_row():
                            dpg.add_text("Inconsciente")
                            dpg.add_text("Resis. Física, Competência")

                        with dpg.table_row():
                            dpg.add_text("Tontura")
                            dpg.add_text("Força, Criatividade, Manipulação")

                        with dpg.table_row():
                            dpg.add_text("Embriaguez")
                            dpg.add_text("Resis. Mental, Competência, Destreza")

                        with dpg.table_row():
                            dpg.add_text("Náusea")
                            dpg.add_text("Força, Criatividade, Competência")

                        with dpg.table_row():
                            dpg.add_text("Hemorragia")
                            dpg.add_text("Força, Resis. Física, Destreza")

                        with dpg.table_row():
                            dpg.add_text("Fratura")
                            dpg.add_text("Força, Resis. Física, Destreza")

                        with dpg.table_row():
                            dpg.add_text("Envenenamento")
                            dpg.add_text("Força, Sobrevivência")

                        with dpg.table_row():
                            dpg.add_text("Fome")
                            dpg.add_text("Força, Sobrevivência")

                        with dpg.table_row():
                            dpg.add_text("Frio/Calor")
                            dpg.add_text("Força, Agilidade")

                        with dpg.table_row():
                            dpg.add_text("Humilhação")
                            dpg.add_text("Resis. Mental, Criatividade, Manipulação")

                        with dpg.table_row():
                            dpg.add_text("Trauma Físico")
                            dpg.add_text("Força, Resis. Física")

                        with dpg.table_row():
                            dpg.add_text("Trauma Psicológico")
                            dpg.add_text("Resis. Mental, Competência, Criatividade")

                        with dpg.table_row():
                            dpg.add_text("Mente Controlada")
                            dpg.add_text("Resis. Mental, Competência, Criatividade")

                        with dpg.table_row():
                            dpg.add_text("Estado crítico de saúde")
                            dpg.add_text("Todos os testes")

                    dpg.add_spacer()
                    dpg.add_text("Armas")
                    with dpg.table(label="Weapons", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Armas")
                        dpg.add_table_column(label="Mod. de Dano")
                        dpg.add_table_column(label="Teste usado")
                        dpg.add_table_column(label="Peso")

                        with dpg.table_row():
                            dpg.add_text("Faca/Adaga")
                            dpg.add_text("+15")
                            dpg.add_text("Força")
                            dpg.add_text("0.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Faca/Adaga")
                            dpg.add_text("+15")
                            dpg.add_text("Força")
                            dpg.add_text("0.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Foice")
                            dpg.add_text("+20")
                            dpg.add_text("Força")
                            dpg.add_text("3Kg")

                        with dpg.table_row():
                            dpg.add_text("Espada")
                            dpg.add_text("+30")
                            dpg.add_text("Força")
                            dpg.add_text("2.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Espada longa (2-mãos)")
                            dpg.add_text("+40")
                            dpg.add_text("Força")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Katana (2-mãos)")
                            dpg.add_text("+42")
                            dpg.add_text("Força")
                            dpg.add_text("2.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Machadinho")
                            dpg.add_text("+18")
                            dpg.add_text("Força")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Machado de guerra")
                            dpg.add_text("+33")
                            dpg.add_text("Força")
                            dpg.add_text("4Kg")

                        with dpg.table_row():
                            dpg.add_text("Alabarda/Machado Grande (2-mãos)")
                            dpg.add_text("+35")
                            dpg.add_text("Força")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Marreta (2-mãos)")
                            dpg.add_text("+45")
                            dpg.add_text("Força")
                            dpg.add_text("10Kg")

                        with dpg.table_row():
                            dpg.add_text("Porrete")
                            dpg.add_text("+18")
                            dpg.add_text("Força")
                            dpg.add_text("3Kg")

                        with dpg.table_row():
                            dpg.add_text("Maça dentada")
                            dpg.add_text("+23")
                            dpg.add_text("Força")
                            dpg.add_text("7Kg")

                        with dpg.table_row():
                            dpg.add_text("Chicote")
                            dpg.add_text("+8")
                            dpg.add_text("Força")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Tridente (2-mãos")
                            dpg.add_text("+33")
                            dpg.add_text("Força")
                            dpg.add_text("4Kg")

                        with dpg.table_row():
                            dpg.add_text("Bastão (2-mãos)")
                            dpg.add_text("+9")
                            dpg.add_text("Força")
                            dpg.add_text("1.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Arco curto")
                            dpg.add_text("+16")
                            dpg.add_text("Destreza")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Arco longo")
                            dpg.add_text("+20")
                            dpg.add_text("Destreza")
                            dpg.add_text("4Kg")

                        with dpg.table_row():
                            dpg.add_text("Shuriken")
                            dpg.add_text("+15")
                            dpg.add_text("Destreza")
                            dpg.add_text("0.1Kg")

                        with dpg.table_row():
                            dpg.add_text("Rifle de precisão")
                            dpg.add_text("+80")
                            dpg.add_text("Destreza")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Besta")
                            dpg.add_text("+18")
                            dpg.add_text("Agilidade")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Revólver")
                            dpg.add_text("+28")
                            dpg.add_text("Agilidade")
                            dpg.add_text("1Kg")

                        with dpg.table_row():
                            dpg.add_text("Pistola semi-auto")
                            dpg.add_text("+30")
                            dpg.add_text("Agilidade")
                            dpg.add_text("1Kg")

                        with dpg.table_row():
                            dpg.add_text("Espingarda")
                            dpg.add_text("+40")
                            dpg.add_text("Agilidade")
                            dpg.add_text("1.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Submetralhadora")
                            dpg.add_text("+33")
                            dpg.add_text("Agilidade")
                            dpg.add_text("1.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Rifle de assalto")
                            dpg.add_text("+45")
                            dpg.add_text("Agilidade")
                            dpg.add_text("2Kg")

                    dpg.add_spacer()
                    dpg.add_text("Equipamentos")
                    with dpg.table(label="Armor", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Equipamento")
                        dpg.add_table_column(label="Pontos de Armadura")
                        dpg.add_table_column(label="Peso")

                        with dpg.table_row():
                            dpg.add_text("Traje de peles")
                            dpg.add_text("4")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Traje de couro")
                            dpg.add_text("6")
                            dpg.add_text("2.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Cota de malha")
                            dpg.add_text("13")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Peitoral de ferro")
                            dpg.add_text("20")
                            dpg.add_text("10Kg")

                        with dpg.table_row():
                            dpg.add_text("Colete à prova de balas (leve)")
                            dpg.add_text("30")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Colete à prova de balas (médio)")
                            dpg.add_text("40")
                            dpg.add_text("6Kg")

                        with dpg.table_row():
                            dpg.add_text("Armadura samurai")
                            dpg.add_text("30")
                            dpg.add_text("15Kg")

                        with dpg.table_row():
                            dpg.add_text("Couraça de aço")
                            dpg.add_text("35")
                            dpg.add_text("20Kg")

                        with dpg.table_row():
                            dpg.add_text("Colete à prova de balas (pesado)")
                            dpg.add_text("50")
                            dpg.add_text("10Kg")

                        with dpg.table_row():
                            dpg.add_text("Arm. Cavaleiro")
                            dpg.add_text("60")
                            dpg.add_text("30Kg")

                        with dpg.table_row():
                            dpg.add_text("Escudo de madeira")
                            dpg.add_text("15")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Scutum (escudo romano)")
                            dpg.add_text("18")
                            dpg.add_text("6Kg")

                        with dpg.table_row():
                            dpg.add_text("Broquel (escudo pequeno)")
                            dpg.add_text("12")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Escudo de ferro")
                            dpg.add_text("22")
                            dpg.add_text("5Kg")

                        with dpg.table_row():
                            dpg.add_text("Escudo de aço")
                            dpg.add_text("28")
                            dpg.add_text("4Kg")

                        with dpg.table_row():
                            dpg.add_text("Escudo eletrônico")
                            dpg.add_text("50")
                            dpg.add_text("2Kg")

                        with dpg.table_row():
                            dpg.add_text("Capacete de couro")
                            dpg.add_text("4")
                            dpg.add_text("1Kg")

                        with dpg.table_row():
                            dpg.add_text("Capacete de obras")
                            dpg.add_text("6")
                            dpg.add_text("0.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Capacete militar moderno")
                            dpg.add_text("12")
                            dpg.add_text("1.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Elmo Viking")
                            dpg.add_text("5")
                            dpg.add_text("1.5Kg")

                        with dpg.table_row():
                            dpg.add_text("Elmo de cavaleiro")
                            dpg.add_text("10")
                            dpg.add_text("2Kg")

            with dpg.tab(label="Jogadores"):
                with dpg.group():
                    dpg.add_text("Jogadores da campanha")
                    with dpg.table(label="Players", width=1000, row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Personagem")
                        dpg.add_table_column(label="PdV")
                        dpg.add_table_column(label="PdA")
                        dpg.add_table_column(label="PdE")
                        dpg.add_table_column(label="Traço +")
                        dpg.add_table_column(label="Traço -")
                        dpg.add_table_column(label="Estado")
                        dpg.add_table_column(label="Pts XP")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem1")
                            dpg.add_input_int(tag="pdv1")
                            dpg.add_input_int(tag="armor1")
                            dpg.add_input_int(tag="pde1")
                            dpg.add_input_text(tag="tracoPos1")
                            dpg.add_input_text(tag="tracoNeg1")
                            dpg.add_input_text(tag="estado1")
                            dpg.add_input_int(tag="pts_xp1")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem2")
                            dpg.add_input_int(tag="pdv2")
                            dpg.add_input_int(tag="armor2")
                            dpg.add_input_int(tag="pde2")
                            dpg.add_input_text(tag="tracoPos2")
                            dpg.add_input_text(tag="tracoNeg2")
                            dpg.add_input_text(tag="estado2")
                            dpg.add_input_int(tag="pts_xp2")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem3")
                            dpg.add_input_int(tag="pdv3")
                            dpg.add_input_int(tag="armor3")
                            dpg.add_input_int(tag="pde3")
                            dpg.add_input_text(tag="tracoPos3")
                            dpg.add_input_text(tag="tracoNeg3")
                            dpg.add_input_text(tag="estado3")
                            dpg.add_input_int(tag="pts_xp3")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem4")
                            dpg.add_input_int(tag="pdv4")
                            dpg.add_input_int(tag="armor4")
                            dpg.add_input_int(tag="pde4")
                            dpg.add_input_text(tag="tracoPos4")
                            dpg.add_input_text(tag="tracoNeg4")
                            dpg.add_input_text(tag="estado4")
                            dpg.add_input_int(tag="pts_xp4")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem5")
                            dpg.add_input_int(tag="pdv5")
                            dpg.add_input_int(tag="armor5")
                            dpg.add_input_int(tag="pde5")
                            dpg.add_input_text(tag="tracoPos5")
                            dpg.add_input_text(tag="tracoNeg5")
                            dpg.add_input_text(tag="estado5")
                            dpg.add_input_int(tag="pts_xp5")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem6")
                            dpg.add_input_int(tag="pdv6")
                            dpg.add_input_int(tag="armor6")
                            dpg.add_input_int(tag="pde6")
                            dpg.add_input_text(tag="tracoPos6")
                            dpg.add_input_text(tag="tracoNeg6")
                            dpg.add_input_text(tag="estado6")
                            dpg.add_input_int(tag="pts_xp6")

                        with dpg.table_row():
                            dpg.add_input_text(tag="personagem7")
                            dpg.add_input_int(tag="pdv7")
                            dpg.add_input_int(tag="armor7")
                            dpg.add_input_int(tag="pde7")
                            dpg.add_input_text(tag="tracoPos7")
                            dpg.add_input_text(tag="tracoNeg7")
                            dpg.add_input_text(tag="estado7")
                            dpg.add_input_int(tag="pts_xp7")

                    dpg.add_spacer()
                    dpg.add_separator()
                    dpg.add_spacer()
                    dpg.add_text("Notas")
                    dpg.add_input_text(width=500, height=400, multiline=True, tag="notas_mestre")

            with dpg.tab(label="NPCs"):
                dpg.add_text("NPCs - Non-Player Characters")
                dpg.add_spacer()
                dpg.add_separator()
                dpg.add_spacer()
                with dpg.group():
                    dpg.add_text("Recorrentes")
                    with dpg.table(label="major", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Nome")
                        dpg.add_table_column(label="Dificuldade")
                        dpg.add_table_column(label="Pontos de Vida")
                        dpg.add_table_column(label="Pontos de Energia")
                        dpg.add_table_column(label="Experiência")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome1")
                            dpg.add_input_int(tag="major_dif1")
                            dpg.add_input_text(tag="major_vida1")
                            dpg.add_input_text(tag="major_energia1")
                            dpg.add_input_text(tag="major_xp1")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome2")
                            dpg.add_input_int(tag="major_dif2")
                            dpg.add_input_text(tag="major_vida2")
                            dpg.add_input_text(tag="major_energia2")
                            dpg.add_input_text(tag="major_xp2")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome3")
                            dpg.add_input_int(tag="major_dif3")
                            dpg.add_input_text(tag="major_vida3")
                            dpg.add_input_text(tag="major_energia3")
                            dpg.add_input_text(tag="major_xp3")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome4")
                            dpg.add_input_int(tag="major_dif4")
                            dpg.add_input_text(tag="major_vida4")
                            dpg.add_input_text(tag="major_energia4")
                            dpg.add_input_text(tag="major_xp4")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome5")
                            dpg.add_input_int(tag="major_dif5")
                            dpg.add_input_text(tag="major_vida5")
                            dpg.add_input_text(tag="major_energia5")
                            dpg.add_input_text(tag="major_xp5")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome6")
                            dpg.add_input_int(tag="major_dif6")
                            dpg.add_input_text(tag="major_vida6")
                            dpg.add_input_text(tag="major_energia6")
                            dpg.add_input_text(tag="major_xp6")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome7")
                            dpg.add_input_int(tag="major_dif7")
                            dpg.add_input_text(tag="major_vida7")
                            dpg.add_input_text(tag="major_energia7")
                            dpg.add_input_text(tag="major_xp7")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome8")
                            dpg.add_input_int(tag="major_dif8")
                            dpg.add_input_text(tag="major_vida8")
                            dpg.add_input_text(tag="major_energia8")
                            dpg.add_input_text(tag="major_xp8")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome9")
                            dpg.add_input_int(tag="major_dif9")
                            dpg.add_input_text(tag="major_vida9")
                            dpg.add_input_text(tag="major_energia9")
                            dpg.add_input_text(tag="major_xp9")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome10")
                            dpg.add_input_int(tag="major_dif10")
                            dpg.add_input_text(tag="major_vida10")
                            dpg.add_input_text(tag="major_energia10")
                            dpg.add_input_text(tag="major_xp10")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome11")
                            dpg.add_input_int(tag="major_dif11")
                            dpg.add_input_text(tag="major_vida11")
                            dpg.add_input_text(tag="major_energia11")
                            dpg.add_input_text(tag="major_xp11")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome12")
                            dpg.add_input_int(tag="major_dif12")
                            dpg.add_input_text(tag="major_vida12")
                            dpg.add_input_text(tag="major_energia12")
                            dpg.add_input_text(tag="major_xp12")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome13")
                            dpg.add_input_int(tag="major_dif13")
                            dpg.add_input_text(tag="major_vida13")
                            dpg.add_input_text(tag="major_energia13")
                            dpg.add_input_text(tag="major_xp13")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome14")
                            dpg.add_input_int(tag="major_dif14")
                            dpg.add_input_text(tag="major_vida14")
                            dpg.add_input_text(tag="major_energia14")
                            dpg.add_input_text(tag="major_xp14")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome15")
                            dpg.add_input_int(tag="major_dif15")
                            dpg.add_input_text(tag="major_vida15")
                            dpg.add_input_text(tag="major_energia15")
                            dpg.add_input_text(tag="major_xp15")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome16")
                            dpg.add_input_int(tag="major_dif16")
                            dpg.add_input_text(tag="major_vida16")
                            dpg.add_input_text(tag="major_energia16")
                            dpg.add_input_text(tag="major_xp16")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome17")
                            dpg.add_input_int(tag="major_dif17")
                            dpg.add_input_text(tag="major_vida17")
                            dpg.add_input_text(tag="major_energia17")
                            dpg.add_input_text(tag="major_xp17")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome18")
                            dpg.add_input_int(tag="major_dif18")
                            dpg.add_input_text(tag="major_vida18")
                            dpg.add_input_text(tag="major_energia18")
                            dpg.add_input_text(tag="major_xp18")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome19")
                            dpg.add_input_int(tag="major_dif19")
                            dpg.add_input_text(tag="major_vida19")
                            dpg.add_input_text(tag="major_energia19")
                            dpg.add_input_text(tag="major_xp19")

                        with dpg.table_row():
                            dpg.add_input_text(tag="major_nome20")
                            dpg.add_input_int(tag="major_dif20")
                            dpg.add_input_text(tag="major_vida20")
                            dpg.add_input_text(tag="major_energia20")
                            dpg.add_input_text(tag="major_xp20")
                    
                    dpg.add_spacer()
                    dpg.add_text("Temporários")
                    with dpg.table(label="Temporary", row_background=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
                        dpg.add_table_column(label="Nome")
                        dpg.add_table_column(label="Dificuldade")
                        dpg.add_table_column(label="Pontos de Vida")
                        dpg.add_table_column(label="Pontos de Energia")
                        dpg.add_table_column(label="Experiência")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome1")
                            dpg.add_input_int(tag="temp_dif1")
                            dpg.add_input_text(tag="temp_vida1")
                            dpg.add_input_text(tag="temp_energia1")
                            dpg.add_input_text(tag="temp_xp1")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome2")
                            dpg.add_input_int(tag="temp_dif2")
                            dpg.add_input_text(tag="temp_vida2")
                            dpg.add_input_text(tag="temp_energia2")
                            dpg.add_input_text(tag="temp_xp2")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome3")
                            dpg.add_input_int(tag="temp_dif3")
                            dpg.add_input_text(tag="temp_vida3")
                            dpg.add_input_text(tag="temp_energia3")
                            dpg.add_input_text(tag="temp_xp3")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome4")
                            dpg.add_input_int(tag="temp_dif4")
                            dpg.add_input_text(tag="temp_vida4")
                            dpg.add_input_text(tag="temp_energia4")
                            dpg.add_input_text(tag="temp_xp4")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome5")
                            dpg.add_input_int(tag="temp_dif5")
                            dpg.add_input_text(tag="temp_vida5")
                            dpg.add_input_text(tag="temp_energia5")
                            dpg.add_input_text(tag="temp_xp5")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome6")
                            dpg.add_input_int(tag="temp_dif6")
                            dpg.add_input_text(tag="temp_vida6")
                            dpg.add_input_text(tag="temp_energia6")
                            dpg.add_input_text(tag="temp_xp6")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome7")
                            dpg.add_input_int(tag="temp_dif7")
                            dpg.add_input_text(tag="temp_vida7")
                            dpg.add_input_text(tag="temp_energia7")
                            dpg.add_input_text(tag="temp_xp7")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome8")
                            dpg.add_input_int(tag="temp_dif8")
                            dpg.add_input_text(tag="temp_vida8")
                            dpg.add_input_text(tag="temp_energia8")
                            dpg.add_input_text(tag="temp_xp8")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome9")
                            dpg.add_input_int(tag="temp_dif9")
                            dpg.add_input_text(tag="temp_vida9")
                            dpg.add_input_text(tag="temp_energia9")
                            dpg.add_input_text(tag="temp_xp9")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome10")
                            dpg.add_input_int(tag="temp_dif10")
                            dpg.add_input_text(tag="temp_vida10")
                            dpg.add_input_text(tag="temp_energia10")
                            dpg.add_input_text(tag="temp_xp10")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome11")
                            dpg.add_input_int(tag="temp_dif11")
                            dpg.add_input_text(tag="temp_vida11")
                            dpg.add_input_text(tag="temp_energia11")
                            dpg.add_input_text(tag="temp_xp11")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome12")
                            dpg.add_input_int(tag="temp_dif12")
                            dpg.add_input_text(tag="temp_vida12")
                            dpg.add_input_text(tag="temp_energia12")
                            dpg.add_input_text(tag="temp_xp12")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome13")
                            dpg.add_input_int(tag="temp_dif13")
                            dpg.add_input_text(tag="temp_vida13")
                            dpg.add_input_text(tag="temp_energia13")
                            dpg.add_input_text(tag="temp_xp13")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome14")
                            dpg.add_input_int(tag="temp_dif14")
                            dpg.add_input_text(tag="temp_vida14")
                            dpg.add_input_text(tag="temp_energia14")
                            dpg.add_input_text(tag="temp_xp14")

                        with dpg.table_row():
                            dpg.add_input_text(tag="temp_nome15")
                            dpg.add_input_int(tag="temp_dif15")
                            dpg.add_input_text(tag="temp_vida15")
                            dpg.add_input_text(tag="temp_energia15")
                            dpg.add_input_text(tag="temp_xp15")
            
            with dpg.tab(label="Salvar"):
                dpg.add_text("Importante! Salve todas as alterações no botão abaixo!")
                dpg.add_text("Importante! Carregue os dados já salvos ")
                dpg.add_button(label="Salvar", callback=salvar)
                dpg.add_button(label="Carregar", callback=carregar)