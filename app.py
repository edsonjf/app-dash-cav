from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import json

dados = pd.read_csv('Player stats Wyscout - PlayerStats.csv')
dados.Date = dados.Date.apply(lambda linha: pd.to_datetime(linha))
dados = dados.query("Date > '2024-01-01'")
encoding='utf-8'
with open('larerais_cav.json', 'r', encoding=encoding) as f1, open('zagueiros_cav.json', 'r', encoding=encoding) as f2, open('meias_cav.json', 'r', encoding=encoding) as f3, open('atacantes_cav.json', 'r', encoding=encoding) as f4:
    laterais = json.load(f1)
    zagueiros = json.load(f2)
    meias = json.load(f3)
    atacantes = json.load(f4)

arquivo = {**laterais, **zagueiros, **meias, **atacantes}


md_col = 2
md_col1 = 3
por_alt = '500px'
tamanho = '100%'
margin = '5px'

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
# graficos [Ações totais,Remates,Passes,Passes longos,Cruzamentos,Dribbles,Duelos,Duelos aéreos,Perdas,Recuperações,]
# cartoes 'Minutos jogados:', Golos,Assistências,xG,Intercepções,Cartao_amarelo	Cartao_vermelho


app.layout = dbc.Container([
    html.H3('Jogador'),
                dcc.Dropdown(
                    id='nomes-jogadores',
                    options= dados.Nome.unique(),
                    value='frank',
                    style={'width':'40%'}
                ),
    dbc.Row([
        
        dbc.Col([
            dbc.Row([
                
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(
                                        id='foto-jogador', width=200,
                                    )
                                ],),
                                dbc.CardFooter([
                                    html.H3(id='nome-completo'),
                                ])
                            ], style={'textAlign':'center'}),
                            dbc.Card([
                                html.P('Jogos'),
                                html.H2(
                                    id='n-jogos'
                                )
                            ], style={'margin':margin}),
                            dbc.Card([
                                html.P('Titular'),
                                html.H2(
                                    id='titular'
                                )
                            ], style={'margin':margin}),
                            dbc.Card([
                                html.P('Minutos'),
                                html.H2(
                                    id='minutos'
                                )
                            ], style={'margin':margin}),
                            dbc.Card([
                                html.P('Gols'),
                                html.H2(
                                    id='gols'
                                )
                            ], style={'margin':margin}),
                            dbc.Card([
                                html.P('Assistência'),
                                html.H2(
                                    id='assistencia'
                                )
                            ], style={'margin':margin}),
                            dbc.Card([
                                html.P('Amarelos'),
                                html.H2(
                                    id='amarelo'
                                )
                            ], style={'margin':margin}),
                            dbc.Card([
                                html.P('Vermelho'),
                                html.H2(
                                    id='vermelho'
                                )
                            ], style={'margin':margin})
                            
                        ], md=3, style={'textAlign':'center', 'padding':'10px'}),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                    dbc.Row([
                                       dbc.Col([
                                           dbc.Card([
                                               html.H3('Ações'),
                                               dcc.Graph(
                                                   
                                                   id='graf_1',
                                                   style={'width':tamanho,
                                                          'height':tamanho}
                                               )
                                           ], style={'height':por_alt,
                                                     'margin':margin}), 
                                           dbc.Card([
                                               html.H3('Passes'),
                                               dcc.Graph(
                                                   
                                                   id='graf_2',
                                                   style={'width':tamanho,
                                                          'height':tamanho}
                                               )
                                           ], style={'height':por_alt,
                                                     'margin':margin}), 
                                           dbc.Card([
                                               html.H3('Duelos'),
                                               dcc.Graph(
                                                   
                                                   id='graf_5',
                                                   style={'width':tamanho,
                                                          'height':tamanho}
                                               )
                                           ], style={'height':por_alt,
                                                     'margin':margin}),
                                           dbc.Card([
                                               html.H3('Finalizações'),
                                               dcc.Graph(
                                                   
                                                   id='graf_7',
                                                   style={'width':tamanho,
                                                          'height':tamanho}
                                               )
                                           ], style={'height':por_alt,
                                                     'margin':margin}), 
                                           dbc.Card([
                                               html.H3('Perdas'),
                                               dcc.Graph(
                                                   
                                                   id='graf_9',
                                                   style={'width':tamanho,
                                                          'height':tamanho}
                                               )
                                           ], style={'height':por_alt,
                                                     'margin':margin}), 
                                       ],),
                                       
                                       # segunda coluna
                                       dbc.Col([
                                           dbc.Card([
                                               html.H3('Cruzamentos'),
                                               dcc.Graph(
                                                   
                                                   id='graf_3',
                                                   style={'width':tamanho,
                                                          'height':tamanho}
                                               )
                                           ], style={'height':por_alt,
                                                     'margin':margin}),
                                           dbc.Card([
                                               html.H3('Passes Longos'),
                                               dcc.Graph(
                                                   
                                                   id='graf_4',
                                                   style={'width':tamanho,
                                                          'height':tamanho}
                                               )
                                           ], style={'height':por_alt,
                                                     'margin':margin}),
                                           dbc.Card([
                                               html.H3('Duelos aéreos'),
                                               dcc.Graph(
                                                   
                                                   id='graf_6',
                                                   style={'width':tamanho,
                                                          'height':tamanho}
                                               )
                                           ], style={'height':por_alt,
                                                     'margin':margin}),
                                           dbc.Card([
                                               html.H3('Dribles'),
                                               dcc.Graph(
                                                   
                                                   id='graf_8',
                                                   style={'width':tamanho,
                                                          'height':tamanho}
                                               )
                                           ], style={'height':por_alt,
                                                     'margin':margin}),
                                        #    dbc.Card([
                                        #        html.H3('Recuperações'),
                                        #        dcc.Graph(
                                                   
                                        #            id='graf_10',
                                        #            style={'width':tamanho,
                                        #                   'height':tamanho}
                                        #        )
                                        #    ], style={'height':por_alt,
                                        #              'margin':margin}), 
                                       ]), 
                                    ],)
                                ],),
                                
                            ])
                        ])
                    ],style={'textAlign':'center', 'padding':'50px'})
                ])
            ])
        ], )
    ])
], fluid=True)


@app.callback(
    [Output('foto-jogador', 'src'),
     Output('nome-completo', 'children'),
     Output('n-jogos', 'children'),
     Output('titular', 'children'),
     Output('minutos', 'children'),
     Output('gols', 'children'),
     Output('assistencia', 'children'),
     Output('amarelo', 'children'),
     Output('vermelho', 'children'),
     Output('graf_1', 'figure'),
     Output('graf_2', 'figure'),
     Output('graf_3', 'figure'),
     Output('graf_4', 'figure'),
     Output('graf_5', 'figure'),
     Output('graf_6', 'figure'),
     Output('graf_7', 'figure'),
     Output('graf_8', 'figure'),
     Output('graf_9', 'figure'),
    #  Output('graf_10', 'figure')
     ],
    [Input('nomes-jogadores', 'value')]    
)
def mostrar_pagina(value):
    jpg = ['orlando-junior-', 'amorim']
    imagem = f"assets/2024 - Copa Paulista/{value}.jpg" if value in jpg else f"assets/2024 - Copa Paulista/{value}.png"
    nome = str(value).capitalize()
    data = dados.loc[dados.Nome == value]
    cores = ['green', 'red']
    
    ogol = pd.read_json(arquivo[value]['tab_geral_jogador'])
    jogos = ogol.iloc[-1,1]
    titular = ogol.iloc[-1,7]
    minutos = ogol.iloc[-1,6]
    gols = ogol.iloc[-1,9]
    assistencia = ogol.iloc[-1,10]
    amarelo = ogol.iloc[-1,12]
    vermelho = ogol.iloc[-1,13] + ogol.iloc[-1,14]
    
    sucesso = data['Ações totais/bem sucedidos'].sum()
    falha = data['Ações totais'].sum() - sucesso
    figura1 = go.Figure(go.Pie(labels=['Bem sucedido', 'Mal sucedido'], values=[sucesso, falha ], hole=0.4,marker=dict(colors=cores),))
    figura1.add_annotation(x=0,y=1, text=f"Total: {sucesso+falha}", showarrow=False)
    figura1.add_annotation(x=0.001,y=0, text=f'Bem: {sucesso}', showarrow=False)
    figura1.add_annotation(x=1,y=0, text=f'Mal: {falha}', showarrow=False)
    # figura1.update_layout(annotations=[{
    # 'text':f'Sucesso: {sucesso}'}])
    
    # Passes
    passe_sucesso = data['Passes/certos'].sum()
    passe = data['Passes'].sum() - passe_sucesso
    figura2 = go.Figure(go.Pie(labels=['Bem sucedido', 'Mal sucedido'], values=[passe_sucesso, passe ],hole=0.4,marker=dict(colors=cores)))
    figura2.add_annotation(x=0,y=1, text=f"Total: {passe_sucesso+passe}", showarrow=False)
    figura2.add_annotation(x=0.001,y=0, text=f'Bem: {passe_sucesso}', showarrow=False)
    figura2.add_annotation(x=1,y=0, text=f'Mal: {sucesso- passe_sucesso}', showarrow=False)
    
    # Cruzamentos
    cruzamento_sucesso = data['Cruzamentos/certos'].sum()
    cruzamento = data['Cruzamentos'].sum() - cruzamento_sucesso
    figura3 = go.Figure(go.Pie(labels=['Bem sucedido', 'Mal sucedido'], values=[cruzamento_sucesso, cruzamento ],hole=0.4,marker=dict(colors=cores)))
    figura3.add_annotation(x=0,y=1, text=f"Total: {cruzamento_sucesso+cruzamento}", showarrow=False)
    figura3.add_annotation(x=0.001,y=0, text=f'Bem: {cruzamento_sucesso}', showarrow=False)
    figura3.add_annotation(x=1,y=0, text=f'Mal: {cruzamento}', showarrow=False)
    
    # Passes Longos
    passe_longo_sucesso = data['Passes longos/certos'].sum()
    passe_longo = data['Passes longos'].sum() - passe_longo_sucesso
    figura4 = go.Figure(go.Pie(labels=['Bem sucedido', 'Mal sucedido'], values=[passe_longo_sucesso, passe_longo ],hole=0.4,marker=dict(colors=cores)))
    figura4.add_annotation(x=0,y=1, text=f"Total: {passe_longo_sucesso+passe_longo}", showarrow=False)
    figura4.add_annotation(x=0.001,y=0, text=f'Bem: {passe_longo_sucesso}', showarrow=False)
    figura4.add_annotation(x=1,y=0, text=f'Mal: {passe_longo}', showarrow=False)
    
    # Duelos
    duelo_longo_sucesso = data['Duelos/ganhos'].sum()
    duelo_longo = data['Duelos'].sum() - duelo_longo_sucesso
    figura5 = go.Figure(go.Pie(labels=['Bem sucedido', 'Mal sucedido'], values=[duelo_longo_sucesso, duelo_longo ],hole=0.4,marker=dict(colors=cores)))
    figura5.add_annotation(x=0,y=1, text=f"Total: {duelo_longo_sucesso+duelo_longo}", showarrow=False)
    figura5.add_annotation(x=0.001,y=0, text=f'Bem: {duelo_longo_sucesso}', showarrow=False)
    figura5.add_annotation(x=1,y=0, text=f'Mal: {duelo_longo}', showarrow=False)
    
    # Duelos aéreos
    duelo_aereo_longo_sucesso = data['Duelos aéreos/ganhos'].sum()
    duelo_aereo_longo = data['Duelos aéreos'].sum()
    figura6 = go.Figure(go.Pie(labels=['Bem sucedido', 'Mal sucedido'], values=[duelo_aereo_longo_sucesso, duelo_aereo_longo ],hole=0.4,marker=dict(colors=cores)))
    figura6.add_annotation(x=0,y=1, text=f"Total: {duelo_aereo_longo_sucesso+duelo_aereo_longo}", showarrow=False)
    figura6.add_annotation(x=0.001,y=0, text=f'Bem: {duelo_aereo_longo_sucesso}', showarrow=False)
    figura6.add_annotation(x=1,y=0, text=f'Mal: {duelo_aereo_longo}', showarrow=False)
    
    # Finalizações
    finalizacao_sucesso = data['Remates/à baliza'].sum()
    finalizacao = data['Remates'].sum()
    figura7 = go.Figure(go.Pie(labels=['Bem sucedido', 'Mal sucedido'], values=[finalizacao_sucesso, finalizacao ],hole=0.4,marker=dict(colors=cores)))
    figura7.add_annotation(x=0,y=1, text=f"Total: {finalizacao_sucesso+finalizacao}", showarrow=False)
    figura7.add_annotation(x=0.001,y=0, text=f'Bem: {finalizacao_sucesso}', showarrow=False)
    figura7.add_annotation(x=1,y=0, text=f'Mal: {finalizacao}', showarrow=False)
    
    # dribles
    drible_sucesso = data['Dribbles/com sucesso'].sum()
    drible = data['Dribbles'].sum()
    figura8 = go.Figure(go.Pie(labels=['Bem sucedido', 'Mal sucedido'], values=[drible_sucesso, drible ],hole=0.4,marker=dict(colors=cores)))
    figura8.add_annotation(x=0,y=1, text=f"Total: {drible_sucesso+drible}", showarrow=False)
    figura8.add_annotation(x=0.001,y=0, text=f'Bem: {drible_sucesso}', showarrow=False)
    figura8.add_annotation(x=1,y=0, text=f'Mal: {drible}', showarrow=False)
    
    # Perdas
    perdas_sucesso = data['Perdas/no seu meio-campo'].sum()
    perdas = data['Perdas'].sum()
    figura9 = go.Figure(go.Pie(labels=['Bem sucedido', 'Mal sucedido'], values=[perdas_sucesso, perdas ],hole=0.4,marker=dict(colors=cores)))
    figura9.add_annotation(x=0,y=1, text=f"Total: {perdas_sucesso+perdas}", showarrow=False)
    figura9.add_annotation(x=0.001,y=0, text=f'Bem: {perdas_sucesso}', showarrow=False)
    figura9.add_annotation(x=1,y=0, text=f'Mal: {perdas}', showarrow=False)
    
    # Recuperações
    # recuperacao_sucesso = data['Recuperações/no meio-campo do adversário'].sum()
    # recuperacao = data['Recuperações'].sum()
    # figura10 = go.Figure(go.Pie(labels=['Bem sucedido', 'Mal sucedido'], values=[recuperacao_sucesso, recuperacao ],hole=0.4,marker=dict(colors=cores)))
    # figura10.add_annotation(x=0,y=1, text=f"Total: {recuperacao_sucesso+recuperacao}", showarrow=False)
    # figura10.add_annotation(x=0.001,y=0, text=f'Bem: {recuperacao_sucesso}', showarrow=False)
    # figura10.add_annotation(x=1,y=0, text=f'Mal: {recuperacao}', showarrow=False)
    
    return imagem, nome, jogos, titular, minutos, gols, assistencia, amarelo, vermelho,figura1, figura2, figura3, figura4, figura5, figura6, figura7, figura8, figura9, #figura10

app.run_server(debug=True)