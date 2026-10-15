---
name: pautas
description: Seleciona as notícias quentes do dia pros dois nichos da casa, empresarial e médico. Roda a coleta (Google Notícias, Google Trends e feeds diretos de 19 veículos), escolhe 10 por nicho e entrega só a manchete e o link de cada uma, pro user escolher qual usar. Use quando o usuário disser /pautas, "pautas do dia", "notícias do dia", "o que está quente hoje". Roda sozinha todo dia às 7h pelo agendamento pautas-do-dia.
---

# /pautas: as notícias quentes do dia pros dois nichos

## Pra que serve

Entregar ao user as notícias que o público já está comentando, pra ele escolher qual vira post (slot HT - NOTÍCIA 19H do calendário e o que mais ele decidir). **A entrega é só manchete e link.** Quem escolhe e quem define o ângulo é o user.

**Pauta quente é o foco.** É topo de funil e puxa engajamento. Notícia técnica também entra, em menor número.

## Passo 1: coletar

```
python3 scripts/noticias/coletar.py
```

- Devolve a lista de cada nicho já ordenada pelo calor, os temas espalhados e o que está em alta no Google Trends. O arquivo completo (manchetes, links, veículos) fica em `conteudo/noticias/_coleta/AAAA-MM-DD.json`.
- O calor sai de quatro sinais: número de veículos que cobriram, destaque no Google Notícias, termo em alta no Trends e recência. As marcas [eleicao], [esporte], [celebridade], [crime] e [loteria] rebaixam o assunto mas não excluem.
- O ranking é a peneira, não a escolha. Quem escolhe é o passo 2.
- Se o Mac passou mais de um dia desligado, rodar com `--horas 48`.
- Fonte fora do ar não trava nada. Anotar no rodapé da edição.

## Passo 2: escolher 10 por nicho

1. **O calor manda.** O que o Brasil está comentando hoje entra primeiro. O maior sinal é o tema espalhado em muitos assuntos (em 28/09/2026 as bets apareceram em 14 matérias diferentes). Tema assim pode ter até duas manchetes na lista, com fatos diferentes.
2. **Escopo largo, sem ser criterioso demais.**
   - Empresarial: empresa, economia, governo, consumo, trabalho, imposto, crédito, tecnologia que mexe no negócio, caso de marca grande. Topo de funil puro serve (exemplo do user: o governo proibiu as bets).
   - Médico: saúde, medicina, regulação (Anvisa, CFM, ANS, Ministério da Saúde), planos, hospitais, clínicas, remédio que virou assunto, estudo que o paciente vai comentar. A mesma superficialidade do empresarial.
3. **Técnica também entra.** Umas 3 por nicho, quando a regra muda o dia a dia de quem tem empresa ou clínica (prazo de imposto, resolução do CFM, cobertura nova da ANS).
4. **Fora por padrão, por risco de marca:** pesquisa eleitoral e briga de candidato (eleição de 2026, 1º turno em 04/10 e 2º em 25/10), esporte, celebridade, crime, clima e loteria. Só entram se o fato mexer com o nicho (exemplo: um médico que ameaçou uma celebridade na internet). Medida de governo entra mesmo em ano de eleição.
5. **Não repetir** manchete da edição de ontem (`conteudo/noticias/` do dia anterior), a não ser que tenha fato novo.
6. **Manchete e link são os da matéria.** A manchete é a do veículo, copiada do JSON da coleta. O link é o da mesma matéria, copiado inteiro do JSON, nunca de texto cortado no terminal. Preferir o link direto do veículo; o do Google Notícias abre a matéria no navegador e serve quando não houver outro. Matéria patrocinada ou requentada (fato de meses atrás publicado hoje) não conta como quente.

## Passo 3: salvar a edição

Arquivo `conteudo/noticias/AAAA-MM-DD.md` (data de Brasília), só com manchete e link:

```markdown
# Pautas do dia · segunda, 28/09/2026

Coleta às 18h06 · 1.539 matérias de 40 fontes nas últimas 30h

## Empresarial

1. [Manchete do veículo](link) · veículo
(até 10)

## Médico

1. [Manchete do veículo](link) · veículo
(até 10)
```

Se alguma fonte falhou, uma linha no rodapé dizendo qual. Rodar de novo no mesmo dia substitui o arquivo do dia.

## Passo 4: fechar

A resposta final é a própria lista, igual ao arquivo: manchete com link, 10 do empresarial e 10 do médico. Não abrir janela nem mandar notificação.

## O que esta skill não faz

- Não escreve gancho, legenda nem texto na voz da casa. A escolha e o ângulo são do user.
- Não usa nada do Cowork como fonte, nem abre a pasta dele. Voz, crenças e público da casa vêm só do guia original (`_contexto/preferencias.md`) e das transcrições do MBV (`_contexto/transcricoes-mbv/`).
- Não chama a API do Instagram e não roda git (nem pull, nem push).
- Não cria post, Manychat nem tarefa no ClickUp.
