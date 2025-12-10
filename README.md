# Halo 5 API Wrapper (Hexagonal Architecture)

This project is a FastAPI-based wrapper for the Halo 5 API, structured using Hexagonal Architecture (Ports & Adapters). It also makes use of Elasticbeanstalk and Github actions to handle the CI/CD.

[![Deploy to AWS Elastic Beanstalk](https://github.com/NicmeisteR/sp-halo5-fastapi-wrapper/actions/workflows/deploy.yml/badge.svg)](https://github.com/NicmeisteR/sp-halo5-fastapi-wrapper/actions/workflows/deploy.yml)

## Structure

- `main.py`: FastAPI entrypoint
- `app/adapters/`: **Adapters Layer**
   - Contains all code that interacts with the outside world (e.g., FastAPI endpoints, external APIs, databases).
   - Example: API routers, HTTP clients, database repositories.
- `app/application/`: **Application Layer**
   - Contains use cases and application-specific logic.
   - Orchestrates domain logic and coordinates adapters.
   - Example: Service functions that call domain logic and interact with adapters.
- `app/domain/`: **Domain Layer**
   - Contains the core business logic, entities, and value objects.
   - Independent of frameworks and external services.
   - Example: Models for Player, ServiceRecord, ArenaStats, and pure business rules.
- `app/config/`: Configuration (API keys, etc.)

---

## Hexagonal Architecture Layer Overview

### Adapters Layer
- Responsible for communication with the outside world (web, database, external APIs).
- Implements interfaces (ports) defined by the application or domain.
- Examples in this project:
   - FastAPI routers (API endpoints)
   - HTTP clients for Halo 5 API

### Application Layer
- Contains use cases and application logic.
- Coordinates domain logic and adapters.
- Implements business workflows, but not the core business rules themselves.
- Examples in this project:
   - Service functions that fetch and process Halo 5 data

### Domain Layer
- Contains the core business logic and rules.
- Defines entities, value objects, and domain services.
- No dependencies on frameworks or external APIs.
- Examples in this project:
   - Models for Player, ArenaStats, ServiceRecord
   - Business rules for interpreting Halo data

---

This separation makes your codebase more maintainable, testable, and adaptable to change. You can swap out adapters (e.g., use a different API or database) without changing your core logic.

## Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the API:
   ```sh
   uvicorn main:app --reload
   ```

## Example Endpoint
- `/api/profile/{player}`: Get Halo 5 player profile (spartan)

## Configuration
- The Halo 5 API key is set in `app/config/settings.py`.

## References
- [Halo 5 API Documentation](https://developer.haloapi.com/apis)


## AWS Elastic Beanstalk CLI (eb) Commands

The AWS Elastic Beanstalk CLI (`eb`) is used to manage your application environments and deployments. Here are some common commands and what they do:

| Command | Description |
|---------|-------------|
| `eb init` | Initialize your project directory with Elastic Beanstalk settings. Run this once per project to set up region, platform, and application. |
| `eb create <env-name>` | Create a new environment (e.g., `eb create halo-api-env`). Deploys your app to a new environment. |
| `eb deploy` | Deploy the latest code changes to the current environment. |
| `eb open` | Open the deployed application in your web browser. |
| `eb status` | Show the status of the current environment (health, URL, etc.). |
| `eb logs` | Retrieve and display logs from the environment. Useful for debugging. |
| `eb terminate <env-name>` | Terminate (delete) an environment and all its resources. |
| `eb setenv VAR=VALUE` | Set environment variables for your application. |

Important to note, eb deploy only deploys what you've commited. Ran into an issue where my changes didn't reflect which is how I found out.

**Example workflow:**
```sh
eb init  # Set up project
eb create halo-api-env  # Create environment and deploy
eb deploy  # Deploy new changes
eb open  # Open app in browser
```

For more, see the [AWS EB CLI documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html).

