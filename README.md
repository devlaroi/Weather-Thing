Um aplicativo **CLI em Python** que detecta automaticamente sua localização e exibe **clima atual**, **previsão de 5 dias** e **qualidade do ar**, usando a API gratuita do **OpenWeatherMap**.

O foco do projeto é fornecer informações meteorológicas detalhadas diretamente no terminal, de forma simples e informativa.

---

## ✨ Funcionalidades

* 📍 **Detecção automática de localização** via IP (com fallback manual)
* 🌡️ **Clima atual**

  * Temperatura atual, mínima e máxima
  * Sensação térmica
  * Umidade, pressão e visibilidade
  * Cobertura de nuvens
* 🌬️ **Dados de vento**

  * Velocidade
  * Direção (cardinal)
  * Rajadas (quando disponíveis)
* 🔥❄️ **Cálculos avançados**

  * Índice de calor (Heat Index)
  * Sensação térmica por vento (Wind Chill)
* 🌅 **Horários locais**

  * Nascer e pôr do sol ajustados ao fuso horário
* 🌫️ **Qualidade do ar (AQI)**

  * Classificação (Good → Very Poor)
  * Recomendações de saúde
* 📆 **Previsão de 5 dias**

  * Intervalos de 3 horas
  * Temperatura, sensação térmica
  * Probabilidade de precipitação
  * Chuva, neve e vento

---

## 🧰 Tecnologias Utilizadas

* Python 3
* [`requests`](https://docs.python-requests.org/)
* [`pytz`](https://pypi.org/project/pytz/)
* API do [OpenWeatherMap](https://openweathermap.org/api)
* Serviço de geolocalização via IP (`ipinfo.io`)

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/weather-cli.git
cd weather-cli
```

2. Instale as dependências:

```bash
pip install requests pytz
```

---

## 🔑 Configuração da API

Este projeto usa a **API gratuita do OpenWeatherMap**.

1. Crie uma conta em:
   [https://openweathermap.org/api](https://openweathermap.org/api)
2. Gere sua **API Key**
3. Substitua a chave no código:

```python
api_key = 'SUA_API_KEY_AQUI'
```

⚠️ **Importante:** Não é recomendado commitar sua API key em repositórios públicos.

---

## ▶️ Como Usar

Execute o script:

```bash
python weather.py
```

O programa irá:

1. Testar a validade da API key
2. Detectar automaticamente sua localização
3. Buscar dados meteorológicos atuais
4. Exibir previsão detalhada de 5 dias
5. Mostrar informações de qualidade do ar (quando disponíveis)

---

## 🧠 Observações

* Caso a detecção automática falhe, o programa solicita os dados manualmente
* A API gratuita pode ter limitações de disponibilidade para qualidade do ar em algumas regiões
* Todos os horários são ajustados para o **fuso local detectado**

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**.
Sinta-se à vontade para usar, modificar e distribuir.

---

## 🚀 Próximas Ideias (Opcional)

* Exportar dados para JSON ou CSV
* Interface gráfica (GUI)
* Cache local para reduzir chamadas à API
* Suporte a múltiplos idiomas
* Alertas meteorológicos

---

