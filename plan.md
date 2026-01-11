# 23-Day Python Mastery Plan (Flexible Schedule)

## Table of Contents

- [Day 0: Setup & Preparation](#day-0-setup--preparation)
- [Week 1: Foundations & Python's Object Model](#week-1-foundations--pythons-object-model)
- [Week 2: Advanced Patterns & Professional Development](#week-2-advanced-patterns--professional-development)
- [Week 3: Concurrency, Performance & Production](#week-3-concurrency-performance--production)
- [Resources](#resources-to-supplement-learning)
- [Success Metrics](#success-metrics)
- [Daily Habits](#daily-habits)

---

## Day 0: Setup & Preparation

### SETUP
By the end of setup, can you answer:

- What Python version are you using and why?
- What's the difference between `pip` and `pip3`?
- How do virtual environments work?
- What are `pyproject.toml` and `requirements.txt` for?

### CODE

- Install Python 3.11+ (or latest stable version)
- Set up a virtual environment: `python -m venv venv`
- Activate it: `source venv/bin/activate` (Unix) or `venv\Scripts\activate` (Windows)
- Create a GitHub repository named `python-mastery-jan-2026`
- Set up folder structure: `/week1`, `/week2`, `/week3`
- Install development tools: `pip install pytest black ruff mypy`
- Create `day0/hello.py` with a simple program
- Write `day0/test_hello.py` with one test using pytest
- Run `pytest -v` to verify setup works
- Create `.gitignore` for Python projects
- Commit everything to git

**Tip:** Add a `README.md` documenting your learning journey. Future you will appreciate it.

---

## Week 1: Foundations & Python's Object Model

### Day 1: Types, Variables & The Object Model

#### READ
By the end, can you answer:

- What does "everything is an object" mean in Python?
- What's the difference between mutable and immutable types?
- How do `int`, `float`, `str`, `bool`, `None` work?
- What is dynamic typing vs static typing?
- How does Python handle integer overflow (spoiler: it doesn't)?
- What are type hints and why use them?

#### CODE: Build a type inspection tool

- Create `week1/day1/typeinspector.py`
- Build a function `inspect_value(val)` that prints:
  - Type, id, size in memory
  - Whether it's mutable/immutable
  - All methods available (use `dir()`)
- Test with: integers, strings, lists, tuples, sets, dicts
- Add type hints to all functions
- Run `mypy` to check type correctness
- Write tests in `test_typeinspector.py`

**Tip:** Use `sys.getsizeof()`, `type()`, `id()`, and `isinstance()`. Discover how Python stores different types.

### Day 2: Collections & Data Structures

#### READ
By the end, can you answer:

- What's the difference between lists, tuples, and arrays?
- How do dictionaries work internally (hash tables)?
- When should you use sets vs lists?
- What are list comprehensions and when are they better than loops?
- What is the complexity (Big O) of common operations on lists/dicts/sets?
- How does slicing work and what are slice objects?

#### CODE: Implement custom data structures

- Create `week1/day2/datastructures.py`
- Implement a `Stack` class using a list
- Implement a `Queue` class using `collections.deque`
- Implement a `LRUCache` class (fixed size, evicts least recently used)
- Create a `CircularBuffer` class
- Write comprehensive tests for each structure
- Add benchmarks comparing your implementations to built-ins

**Tip:** Use `collections` module. Compare `list.pop(0)` vs `deque.popleft()` performance.

### Day 3: Control Flow & Iteration

#### READ
By the end, can you answer:

- What's the difference between `is` and `==`?
- How does Python's `for` loop differ from other languages?
- What are iterators and iterables?
- What is the iterator protocol (`__iter__` and `__next__`)?
- When should you use `while` vs `for`?
- What are `else` clauses on loops and when are they useful?

#### CODE: Build a configuration validator

- Create `week1/day3/config_validator.py`
- Read a JSON/YAML config file
- Validate required fields exist
- Check types match expected schema
- Support nested structures
- Provide helpful error messages (which field, what's wrong, line number if possible)
- Use custom exceptions for different validation errors
- Write tests with valid and invalid configs

**Tip:** Use `pathlib` for file handling. Create a schema dict to validate against.

### Day 4: Functions & Functional Programming

#### READ
By the end, can you answer:

- What are first-class functions?
- How do closures work in Python?
- What are `*args` and `**kwargs`?
- What's the difference between positional, keyword, and positional-only arguments?
- How do decorators work?
- What are lambda functions and when should you use them?
- What is function scope (LEGB rule)?

#### CODE: Create a decorator library

- Create `week1/day4/decorators.py`
- Implement `@timer` - measures function execution time
- Implement `@retry(max_attempts=3, delay=1)` - retries on exception
- Implement `@memoize` - caches function results
- Implement `@validate_types` - checks type hints at runtime
- Implement `@rate_limit(calls=5, period=1)` - limits function calls
- Write tests demonstrating each decorator
- Create a `main.py` showing all decorators in action

**Tip:** Use `functools.wraps` to preserve function metadata. Learn about closure variables.

### Day 5: Object-Oriented Programming

#### READ
By the end, can you answer:

- What are classes and instances?
- What's the difference between instance variables and class variables?
- How does inheritance work in Python?
- What is `super()` and when do you use it?
- What are dunder methods (magic methods)?
- What is the difference between `@classmethod`, `@staticmethod`, and instance methods?
- What are properties and how do they work?

#### CODE: Build an OOP banking system

- Create `week1/day5/banking.py`
- Create `Account` base class with balance, deposit, withdraw
- Create `SavingsAccount` and `CheckingAccount` subclasses
- Implement `__str__`, `__repr__`, `__eq__` methods
- Use `@property` for balance (read-only from outside)
- Implement `AccountManager` to manage multiple accounts
- Add transaction history using a list
- Write tests for all account operations
- Add type hints throughout

**Tip:** Use ABC (Abstract Base Classes) for the base Account. Make methods raise `NotImplementedError` where appropriate.

### Day 6: Advanced OOP & Design Patterns

#### READ
By the end, can you answer:

- What is composition vs inheritance?
- What are abstract base classes (ABC)?
- What is duck typing?
- What are protocols (PEP 544)?
- How does multiple inheritance work (MRO)?
- What are dataclasses and when should you use them?
- What are metaclasses (basic understanding)?

#### CODE: Design a plugin system

- Create `week1/day6/plugins/`
- Define a `Plugin` protocol/ABC with `name`, `version`, `execute()`
- Implement three plugins: `TextProcessorPlugin`, `DataValidatorPlugin`, `NotificationPlugin`
- Use `dataclasses` for plugin configuration
- Create `PluginManager` with registration and discovery
- Implement plugin dependency resolution
- Write tests verifying the plugin interface
- Use `importlib` to dynamically load plugins

**Tip:** Look at `typing.Protocol` and `abc.ABC`. Study how real plugin systems work (pytest plugins, for example).

### Day 7: Review & Testing Deep Dive

#### READ
By the end, can you answer:

- What are the key Python concepts from this week?
- What's the difference between unit, integration, and functional tests?
- What are fixtures in pytest?
- How do you use parametrize for multiple test cases?
- What is test coverage and how do you measure it?
- What are mocks and when should you use them?

#### CODE: Write comprehensive tests

- Pick your best project from this week (probably banking or plugins)
- Write pytest fixtures for common test setup
- Use `@pytest.mark.parametrize` for table-driven tests
- Add integration tests that test multiple components together
- Use `unittest.mock` to mock external dependencies
- Run with coverage: `pytest --cov=. --cov-report=html`
- Aim for >85% coverage
- Set up `pytest.ini` with your preferred settings

**Tip:** Study pytest's documentation. Learn about fixtures, markers, and parametrization.

---

## Week 2: Advanced Patterns & Professional Development

### Day 8: Error Handling & Context Managers

#### READ
By the end, can you answer:

- What's the difference between exceptions and errors?
- How does `try/except/else/finally` work?
- What is exception chaining (`raise ... from`)?
- What are context managers and why use them?
- How do you create a context manager with `__enter__` and `__exit__`?
- What is `contextlib` and when should you use it?
- What are best practices for custom exceptions?

#### CODE: Build a robust file processor

- Create `week2/day8/file_processor.py`
- Implement custom exceptions: `FileProcessingError`, `ValidationError`, `TransformError`
- Create a context manager `TransactionFile` that:
  - Opens a file for writing
  - Buffers all writes
  - Commits on success, rolls back on error
- Implement retry logic with exponential backoff
- Use `contextlib.contextmanager` decorator
- Add comprehensive error handling and logging
- Write tests that trigger different exception paths

**Tip:** Use `logging` module for proper error logging. Test both success and failure scenarios.

### Day 9: Modules, Packages & Project Structure

#### READ
By the end, can you answer:

- What's the difference between a module and a package?
- How does Python's import system work?
- What is `__init__.py` and when is it needed?
- What are namespace packages?
- How do you structure a Python project?
- What is `pyproject.toml` vs `setup.py`?
- How do you make your package installable?

#### CODE: Create a multi-package library

- Create `week2/day9/datatools/` as your root package
- Structure: `datatools/processing/`, `datatools/validation/`, `datatools/export/`
- Create `pyproject.toml` with metadata and dependencies
- Add `__init__.py` files with clean APIs
- Implement functions in each subpackage
- Create `examples/` directory with usage examples
- Add `README.md` with installation and usage
- Make it pip-installable: `pip install -e .`
- Test importing in different ways

**Tip:** Study popular Python packages on GitHub. See how they structure their code.

### Day 10: Iterators, Generators & Async Basics

#### READ
By the end, can you answer:

- What's the difference between an iterator and a generator?
- How does `yield` work?
- What are generator expressions?
- What is lazy evaluation and why is it useful?
- What are coroutines?
- What's the difference between `yield` and `yield from`?
- How do you chain generators?

#### CODE: Build a data processing pipeline

- Create `week2/day10/pipeline.py`
- Implement generator functions:
  - `read_large_file(filename)` - yields lines one at a time
  - `filter_data(data, predicate)` - filters items
  - `transform_data(data, func)` - transforms each item
  - `batch_data(data, size)` - groups items into batches
- Create a pipeline that processes a large CSV file
- Compare memory usage: generator vs loading entire file
- Implement `send()` and `throw()` on generators
- Write tests for each pipeline stage

**Tip:** Use `memory_profiler` to see the difference. Generators should use constant memory.

### Day 11: Async/Await & Concurrency

#### READ
By the end, can you answer:

- What is async/await in Python?
- What's the difference between concurrency and parallelism?
- What is the event loop?
- What are coroutines, tasks, and futures?
- When should you use `asyncio` vs threading vs multiprocessing?
- What is `async with` and `async for`?
- What are the limitations of async in Python?

#### CODE: Build an async web scraper

- Create `week2/day11/scraper.py`
- Use `aiohttp` to fetch multiple URLs concurrently
- Implement rate limiting (max N concurrent requests)
- Parse HTML responses (use `beautifulsoup4`)
- Store results in async-safe queue
- Add retry logic for failed requests
- Implement graceful shutdown
- Compare performance: sync vs async (time 10 URLs)

**Tip:** Install `aiohttp` and `asyncio`. Learn about `asyncio.gather()` and `asyncio.create_task()`.

### Day 12: Web Development with FastAPI

#### READ
By the end, can you answer:

- What is ASGI vs WSGI?
- How does FastAPI use type hints?
- What are path parameters and query parameters?
- How does dependency injection work in FastAPI?
- What is Pydantic and how does it validate data?
- How do you handle errors in FastAPI?
- What are middleware and how do you use them?

#### CODE: Build a REST API

- Create `week2/day12/api/`
- Install FastAPI and Uvicorn
- Build endpoints: `GET /items`, `POST /items`, `GET /items/{id}`, `DELETE /items/{id}`
- Use Pydantic models for request/response validation
- Implement in-memory storage (dict or list)
- Add proper HTTP status codes
- Implement error handling middleware
- Add request logging middleware
- Write API tests using `httpx`

**Tip:** Use FastAPI's automatic docs at `/docs`. Test with `pytest` and `httpx.AsyncClient`.

### Day 13: Databases & ORMs

#### READ
By the end, can you answer:

- What is an ORM and why use one?
- How does SQLAlchemy work?
- What are sessions and transactions?
- What's the difference between query() and select()?
- How do you define relationships (one-to-many, many-to-many)?
- What is connection pooling?
- What are migrations and why are they important?

#### CODE: Add database to your API

- Install SQLAlchemy and alembic
- Create `week2/day13/api/` (extend day 12)
- Define SQLAlchemy models with relationships
- Set up async database connection
- Replace in-memory storage with database
- Implement CRUD operations
- Add database migrations with Alembic
- Write tests with an in-memory SQLite database

**Tip:** Use SQLAlchemy 2.0 syntax. Learn about `async_sessionmaker` and dependency injection.

### Day 14: Performance Optimization

#### READ
By the end, can you answer:

- What tools can you use to profile Python code?
- What is the GIL and how does it affect performance?
- When should you use multiprocessing vs threading?
- What are the common performance bottlenecks?
- How do you optimize list operations?
- What is `__slots__` and when should you use it?
- How does string concatenation affect performance?

#### CODE: Profile and optimize

- Create `week2/day14/optimizer.py`
- Write a slow function (nested loops, inefficient string concat)
- Profile with `cProfile`: `python -m cProfile -s cumtime optimizer.py`
- Use `line_profiler` for line-by-line profiling
- Use `memory_profiler` to find memory leaks
- Optimize the function (list comprehensions, generators, better algorithms)
- Compare: before and after benchmarks
- Write a report of findings and improvements

**Tip:** Install `line_profiler` and `memory_profiler`. Focus on the 80/20 rule - optimize the slow 20%.

---

## Week 3: Concurrency, Performance & Production

### Day 15: Threading & Multiprocessing

#### READ
By the end, can you answer:

- What is the Global Interpreter Lock (GIL)?
- When is threading useful despite the GIL?
- How does `concurrent.futures` simplify concurrent programming?
- What's the difference between `ThreadPoolExecutor` and `ProcessPoolExecutor`?
- How do you share data between processes?
- What are `Queue`, `Pipe`, `Manager`?
- What are the risks of concurrent programming?

#### CODE: Build a concurrent file processor

- Create `week3/day15/concurrent_processor.py`
- Process multiple large files concurrently
- Implement both threading and multiprocessing versions
- Use `ThreadPoolExecutor` for I/O-bound tasks
- Use `ProcessPoolExecutor` for CPU-bound tasks (e.g., data transformation)
- Implement a progress tracker using `Queue`
- Add proper error handling for worker failures
- Benchmark: serial vs threaded vs multiprocessing

**Tip:** Use `concurrent.futures.as_completed()` to process results as they arrive.

### Day 16: Advanced Async Patterns

#### READ
By the end, can you answer:

- What are async context managers?
- How do you handle errors in async code?
- What is `asyncio.gather()` vs `asyncio.wait()`?
- How do you cancel async tasks?
- What are async generators?
- How does backpressure work in async streams?
- What are best practices for structuring async applications?

#### CODE: Build a real-time data processor

- Create `week3/day16/realtime_processor.py`
- Simulate a stream of events (async generator)
- Process events with multiple async workers
- Implement a fan-out/fan-in pattern
- Add graceful shutdown with task cancellation
- Implement retry with exponential backoff
- Add monitoring: events/sec, errors, queue size
- Use `asyncio.Queue` for buffering

**Tip:** Learn about `asyncio.create_task()`, `task.cancel()`, and handling `CancelledError`.

### Day 17: Testing Strategies

#### READ
By the end, can you answer:

- What's the testing pyramid?
- What are test doubles (mocks, stubs, fakes, spies)?
- How do you test async code?
- What is property-based testing?
- What are mutation tests?
- How do you measure test quality, not just coverage?
- What is TDD and when should you use it?

#### CODE: Write advanced tests

- Create `week3/day17/tests/`
- Write property-based tests using `hypothesis`
- Test your async code from day 16
- Use `pytest-asyncio` for async tests
- Mock external services with `unittest.mock` and `pytest-mock`
- Write integration tests that test multiple components
- Set up test fixtures and factories
- Aim for >90% coverage with meaningful tests

**Tip:** Install `hypothesis` for property-based testing. It finds edge cases you wouldn't think of.

### Day 18: Logging, Monitoring & Observability

#### READ
By the end, can you answer:

- What are the different logging levels?
- How do you configure logging in production?
- What's the difference between logging and monitoring?
- What are structured logs and why use them?
- What is distributed tracing?
- How do you correlate logs across services?
- What metrics should you track?

#### CODE: Add observability to your API

- Extend `week2/day12/api/`
- Set up structured logging (JSON format)
- Add request ID to all logs
- Implement middleware for request/response logging
- Add metrics tracking (requests/sec, latency, errors)
- Use `prometheus_client` to expose metrics
- Add health check endpoint
- Implement distributed tracing with correlation IDs

**Tip:** Use `structlog` for structured logging. Look into OpenTelemetry for tracing.

### Day 19: Security & Best Practices

#### READ
By the end, can you answer:

- What are common security vulnerabilities (OWASP Top 10)?
- How do you validate and sanitize input?
- What is SQL injection and how do you prevent it?
- How do you handle secrets and credentials?
- What is CORS and why does it matter?
- How do you implement authentication and authorization?
- What are security headers?

#### CODE: Secure your API

- Extend your API from week 2
- Add input validation and sanitization
- Implement JWT-based authentication
- Add role-based authorization
- Set up CORS properly
- Add rate limiting per user
- Implement API key rotation
- Add security headers (use `python-security`)
- Write security tests

**Tip:** Use `python-jose` for JWT. Never store passwords in plain text - use `bcrypt` or `argon2`.

### Day 20: Deployment & Containerization

#### READ
By the end, can you answer:

- What is Docker and why use it?
- What's the difference between a container and a virtual machine?
- What is a Dockerfile and how do you write one?
- What are multi-stage builds?
- How do you handle environment variables?
- What is docker-compose?
- What are health checks?

#### CODE: Containerize your application

- Create `week3/day20/`
- Write a `Dockerfile` for your API
- Use multi-stage builds (builder and runtime)
- Create `docker-compose.yml` with API + database
- Add health checks
- Configure environment variables
- Set up volume mounts for development
- Add a `Makefile` for common commands
- Test the containerized application

**Tip:** Keep images small. Use Alpine or slim base images. Never include secrets in the image.

### Day 21: CI/CD & Automation

#### READ
By the end, can you answer:

- What is CI/CD?
- What is GitHub Actions / GitLab CI?
- How do you automate testing?
- What are pre-commit hooks?
- How do you automate code formatting and linting?
- What is semantic versioning?
- How do you automate releases?

#### CODE: Set up automation

- Create `.github/workflows/ci.yml`
- Set up automated testing on push/PR
- Add linting (ruff, black) and type checking (mypy)
- Set up pre-commit hooks
- Add code coverage reporting
- Create a release workflow
- Add badges to README
- Document the CI/CD process

**Tip:** Use `pre-commit` framework. Start simple and add complexity as needed.

### Day 22 - FINAL DAY: Production-Ready Project

#### READ & REFLECT
By the end, can you answer:

- What were the three most important concepts you learned?
- Can you explain async/await and when to use it?
- Do you understand the GIL and its implications?
- Are you comfortable with testing strategies?
- Can you deploy a production-ready application?
- What advanced topics interest you most?

#### CODE: Mini Capstone - Task Queue System

- Create `week3/day22/taskqueue/`
- Build a distributed task queue (simplified Celery)
- Components:
  - **Producer**: Submits tasks to queue
  - **Queue**: Redis-based task storage
  - **Worker**: Processes tasks concurrently
  - **Result backend**: Stores task results
- Features:
  - Async task submission
  - Multiple workers
  - Task retry on failure
  - Task status tracking
  - Graceful shutdown
- Add monitoring dashboard (optional: Streamlit)
- Containerize with Docker Compose
- Write comprehensive tests
- Document architecture and usage

**Tip:** Use `redis-py` for the queue. Combine everything you've learned: async, concurrency, OOP, testing, logging, Docker.

---

## Resources to Supplement Learning

- [Python Official Docs](https://docs.python.org/3/)
- [Real Python](https://realpython.com) - Excellent tutorials
- [Python Enhancement Proposals (PEPs)](https://peps.python.org/)
- "Fluent Python" by Luciano Ramalho
- "Effective Python" by Brett Slatkin
- [Full Stack Python](https://www.fullstackpython.com)
- [Python Speed](https://pythonspeed.com) - Performance tips
- [ArjanCodes YouTube](https://www.youtube.com/c/ArjanCodes) - Best practices

---

## Success Metrics

By the end, you should confidently answer YES to:

- ✅ Can I explain Python's object model and memory management?
- ✅ Can I write clean, tested, type-hinted code?
- ✅ Do I understand async/await and when to use it?
- ✅ Can I optimize Python code for performance?
- ✅ Can I build and deploy production-ready applications?
- ✅ Do I feel ready to contribute to real-world Python projects?

---

## Daily Habits

- **Night before:** Review tomorrow's questions to prime your brain
- **Session start:** Environment ready, distractions eliminated
- **During coding:** Write tests first (TDD when appropriate)
- **After session:** Run `black`, `ruff`, `mypy` before committing
- **End of day:** Commit to GitHub with descriptive messages
- **Weekly:** Review what worked, what didn't, adjust pace as needed

**Remember:** Consistency beats intensity. 1-2 focused hours daily > marathon sessions.