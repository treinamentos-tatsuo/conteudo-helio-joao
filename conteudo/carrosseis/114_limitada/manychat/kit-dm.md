# Kit Manychat — carrossel 114 ("Sua empresa é limitada? O SEU CPF NÃO É.")

- **Publicação:** a definir pelo user. Montar STOPPED quando o horário for conhecido; ativar em até 5 min da publicação.
- **Caminho de CTA (regra de 09/09):** **diagnóstico gratuito**. Quinto post do caminho (100 = 1, 103 = 2, 106 = 3, 111 = 4, 114 = 5).
- **Palavra-chave:** DIAGNÓSTICO, palavra FIXA do caminho, SEIS grafias: `DIAGNOSTICO, diagnostico, Diagnostico, DIAGNÓSTICO, diagnóstico, Diagnóstico`.
- **Rastreio:** código numérico sequencial no UTM. Este post = **5**.
- **Link:** `https://rtc.tatsuoacademy.com/diagnostico?utm_source=manychat&utm_medium=dm&utm_campaign=5`
- **Colisão:** checar "diagnos" na lista antes de duplicar (esperado: DIAGNOSTICO-1, -3, -4 e a do aniversário, todas específicas; sem global).
- **Automação:** por POST ESPECÍFICO. Nome: `IG | AAAA-MM-DD | DIAGNOSTICO-5 | o seu CPF nao e limitado` (data = dia da publicação).
- **Modelo a duplicar:** a `IG | 2026-09-11 | DIAGNOSTICO-4 | quebra com a loja cheia` (mesmas 6 grafias; só muda nome, DM e o rabo do UTM: End + Backspace + `5`).

## Mensagem da DM (100 caracteres)
Sua empresa é limitada, o seu CPF não é. Quer saber se ela te paga pelo risco? Diagnóstico gratuito.

## Texto do botão
`>> Quero ver <<` (herdado)

## Operação
1. Antes da publicação: duplicar → renomear → conferir as 6 grafias → DM (por `form_input`) → link: End + Backspace + `5` no modal do botão → conferir em 3 passadas → Atualização → deixar STOPPED.
2. Com o post no ar: Editar → grade 'Mostrar Todos' → capa "Sua empresa é limitada? / O SEU CPF NÃO É." (dono de avental na bancada com os sapatinhos de criança) → conferir preview (legenda "Tem uma palavra na placa da sua empresa que vale menos do que você pagou por ela") → UTM (`End`: `utm_campaign=5`) → Atualização → Ativar → print. Preencher `data_publicacao` na ficha do 114.

## Montagem e ativação (12/09, ~13h25) — LIVE
- Nome final: `IG | 2026-09-12 | DIAGNOSTICO-5 | o seu CPF nao e limitado`. URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260912162254_957144
- Duplicada da DIAGNOSTICO-4, renomeada, post 114 selecionado na grade (primeiro card), DM nova, UTM `=5`, Atualização, Ativar. Tudo numa passada, ~2 min depois da publicação estar indexada.
