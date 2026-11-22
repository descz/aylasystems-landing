# Revisão jurídica do site Ayla Systems

Este documento é um roteiro para o advogado responsável. Ele não substitui a revisão: os textos de LGPD, Termos de uso e Privacidade publicados hoje foram redigidos pela operação e nunca passaram por análise jurídica.

## Antes da revisão

Dados que faltam no site e precisam ser confirmados:

- Razão social e CNPJ da empresa que opera o site.
- Endereço para correspondência e foro.
- Nome e contato do encarregado de dados (DPO), ou a decisão de usar o canal `business@aylasystems.com`.
- Base legal adotada para o formulário (consentimento ou legítimo interesse) e para o Google Analytics.
- Prazo de retenção dos leads recebidos por e-mail.
- Lista de operadores: Zoho (e-mail e hospedagem de caixa), Vercel (hospedagem), Google (Tag Manager e Analytics).
- Se haverá coleta de dados sensíveis em atendimentos de saúde; hoje o site não coleta.

## Arquivos a revisar

- `lgpd.html`: princípios, direitos e canal de contato.
- `termos.html`: uso do site, propriedade intelectual e limitação de responsabilidade.
- `privacidade.html`: cookies, analytics, formulário, compartilhamento e transferência internacional.

## Pontos que o advogado deve fechar

1. **Consentimento de cookies.** O Google Analytics carrega assim que a página abre, sem faixa de consentimento. A LGPD e a orientação da ANPD tratam cookies de medição como dependentes de consentimento. Definir: implementar faixa de consentimento, usar modo de consentimento do Google ou remover o Analytics.
2. **Transferência internacional.** Zoho, Vercel e Google processam dados fora do Brasil. A política precisa nomear os países ou a cláusula usada.
3. **Formulário.** O site envia nome, empresa, segmento e WhatsApp para um servidor na Vercel e por e-mail para a Zoho. Confirmar base legal, aviso no momento da coleta e retenção.
4. **Direitos do titular.** Definir prazo de resposta e procedimento para exclusão.
5. **Termos.** Confirmar se há contratação pelo site ou apenas contato comercial; hoje o site é institucional.
6. **Dados da empresa.** Inserir razão social, CNPJ e endereço, ou confirmar que a operação é feita como pessoa física.
7. **Menores.** Confirmar se o serviço pode ser usado por menores e como isso é tratado.

## O que já está correto

- Fontes hospedadas no próprio domínio, sem chamadas a terceiros.
- Sem pixels de redes sociais.
- Formulário sem banco de dados próprio.
- HTTPS com HSTS e política de segurança restritiva.
