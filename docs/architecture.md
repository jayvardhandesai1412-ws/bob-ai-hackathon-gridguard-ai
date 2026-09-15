# Architecture

```mermaid
graph TD
A[User] --> B[React Dashboard]
B --> C[Flask Backend]
C --> D[Sensor Data]
C --> E[Weather Data]
C --> F[Risk Engine]
F --> B
```
