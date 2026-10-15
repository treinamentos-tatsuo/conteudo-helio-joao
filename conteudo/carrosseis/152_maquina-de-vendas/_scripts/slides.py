"""Post 152 — slides renderizados: 1 (capa = hub), 3 e 4. Slides 2 e 5 levam foto do Hélio e são montados à mão pelo user."""
import sys, pathlib
sys.path.insert(0, '/Users/pedrohenrique/Documents/tatsuo-carrossel/.claude/skills/carrossel/modelos/infografico')
import build

POST = pathlib.Path(__file__).resolve().parents[1]

S2 = dict(
    titulo='DOIS TIPOS DE MÁQUINA', faixa='QUAL DELAS GIRA NA SUA EMPRESA?',
    colunas=dict(top=410, altura=540, largura=440, gap_x=40, texto_px=32, itens=[
        dict(titulo='DEPENDENTE<br>DO DONO', texto='O dono empurra todo dia. No dia em que ele sai, a máquina para.'),
        dict(titulo='INDEPENDENTE<br>DO DONO', texto='Gira sozinha. O dono conduz de longe, não empurra.'),
    ]),
    caixa=dict(top=1045, texto='O objetivo não é fazer mais. É comandar melhor.', px=27, largura=860),
    css='.coluna{display:flex;flex-direction:column;justify-content:center} .coluna h3{font-size:60px} #col-1{background:linear-gradient(165deg,#2b2b2b 0%,#1c1c1c 100%)}',
)

S3 = dict(
    titulo='AS 6 ENGRENAGENS', faixa='DA MÁQUINA DE VENDAS',
    hub=dict(cx=540, cy=770, d=320, fonte=46, texto='ELAS GIRAM<br>JUNTAS,<br>NÃO EM FILA', nos=[
        dict(icone='target-arrow', rotulo='1 · METAS', desc='O número que a máquina precisa produzir.', x=180, y=360, w=320),
        dict(icone='speakerphone', rotulo='2 · QUANTITATIVO', desc='Quantas oportunidades entram.', x=900, y=360, w=320),
        dict(icone='list-check', rotulo='3 · QUALITATIVO', desc='Quantas viram venda, e por quê.', x=180, y=660, w=320),
        dict(icone='gauge', rotulo='4 · CONTROLE', desc='O que se mede e se corrige.', x=900, y=660, w=320),
        dict(icone='flame', rotulo='5 · AMBIENTE', desc='O que a empresa faz toda semana.', x=180, y=960, w=320),
        dict(icone='flag-3', rotulo='6 · LIDERANÇA', desc='Quem responde pela máquina todo dia.', x=900, y=960, w=320),
    ]),
)

S4 = dict(
    titulo='PERGUNTAS DE DONO', faixa='RESPONDA PARA A SUA EMPRESA',
    cards=dict(top=380, altura=180, largura=440, gap_x=40, gap_y=70, corpo_px=22.5, itens=[
        ('01', 'METAS', 'Sua empresa tem meta? De onde saiu esse número?'),
        ('02', 'QUANTITATIVO', 'Quantas oportunidades novas entraram no mês passado?'),
        ('03', 'QUALITATIVO', 'Existe um jeito certo de vender, ou cada um vende como aprendeu?'),
        ('04', 'CONTROLE', 'Que esforços são acompanhados hoje, além do faturamento?'),
        ('05', 'AMBIENTE', 'O ambiente de vendas influencia o moral do time?'),
        ('06', 'LIDERANÇA', 'Quem assume a responsabilidade de fazer tudo isso acontecer?'),
    ]),
    caixa=dict(top=1096, texto='Onde a resposta ficou vaga, a venda ainda depende do esforço de alguém. Máquina de vendas é o que faz a venda acontecer mesmo sem essa pessoa empurrando.', px=23, largura=920),
)

if __name__ == '__main__':
    d = build.escrever(POST, {1: S3, 3: S2, 4: S4})   # 1 = capa (hub); 2 e 5 = foto do Hélio, montagem manual
    print(d)
