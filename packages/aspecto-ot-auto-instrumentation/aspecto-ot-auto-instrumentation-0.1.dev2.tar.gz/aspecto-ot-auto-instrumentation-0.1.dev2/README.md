<p align="center">
  <img src="https://logo.aspecto.io/logo-v2.png"  style="width: 300px" width="300"/>
</p>

<p align="center" style="font-size: 30px">
  Aspecto OpenTelemetry Auto Instrumentation
</p>

<p align="center" style="font-size: 22px">
<p align="center">
  <a href="https://pypi.org/project/aspecto-ot-auto-instrumentation"><img src="https://badge.fury.io/py/aspecto-ot-auto-instrumentation.svg" alt="Aspecto@PyPi"/></a>
</p>
</p>

---
<br/>

This package is using OpenTelemetry to export your api traces to Aspecto.  
Supported integrations:
* Flask
* requests

## Installation
    pip install aspecto-ot-auto-instrumentation


## Usage
```python
from opentelemetry.aspecto import AspectoInstrumentor

AspectoInstrumentor(
    service_name="demo-flask",
    aspecto_auth="your-aspecto-token",
    env="development" 
).instrument()
```

`AspectoInstrumentor` params:  
* **service_name** - mandatory, the name of the service you're instrumenting
* **aspecto_auth** - your token that was obtained from [aspecto website](https://app.aspecto.io/app/integration).  
Alternatively, your can pass it as `ASPECTO_AUTH` env param, or place an `aspecto.json` file at the project root, containing an object with `token` key.
* **env** - optional, if none provided we will use `empty`.



## References

* [Aspecto](https://app.aspecto.io)
* [OpenTelemetry Project](https://opentelemetry.io/)
