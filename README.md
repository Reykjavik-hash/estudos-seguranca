# 04 · TOTP e MFA

## O que é
**TOTP** (Time-based One-Time Password) é o código de 6 dígitos que muda a cada 30 segundos nos aplicativos autenticadores.

## Como funciona
1. Servidor e celular compartilham um **segredo** (o QR code do cadastro).
2. Ambos calculam: `HMAC(segredo, horário ÷ 30)`.
3. Sem trocar mensagens, os dois chegam ao **mesmo número**.

## Experimento
O arquivo [`totp.py`](totp.py) reimplementa o algoritmo em Python. Cadastrei o segredo de teste num app autenticador e **os códigos ficaram idênticos**.

## Comparação dos métodos

| Método | Ponto forte | Ponto fraco |
|---|---|---|
| SMS | Fácil | SIM swap e interceptação |
| App (TOTP) | Funciona offline | Não resiste a phishing em tempo real (AiTM) |
| Passkey / chave física (FIDO2) | Só responde ao domínio real | Exige dispositivo compatível |

## O que aprendi (com minhas palavras)
 O TOTP é um método de autenticação em dois fatores (A2F). O app e o servidor compartilham uma chave secreta e, a partir dela e do horário atual, ambos calculam um código de uso único que dura geralmente 30 segundos. Ele protege contra invasões em que o atacante só descobriu a senha. Porém, não impede ataques com sites espelhados (AiTM): a vítima digita o código na página falsa e o atacante o usa imediatamente no site verdadeiro. Já a passkey só funciona no domínio real cadastrado, então na página falsa ela simplesmente não responde.
