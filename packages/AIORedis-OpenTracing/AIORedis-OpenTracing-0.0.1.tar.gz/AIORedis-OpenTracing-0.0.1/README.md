# AIORedis-OpenTracing

This package enables distributed tracing for the Python asyncio Redis library via `The OpenTracing Project`.
It is heavily influenced by the [Redis Opentracing implementation](https://github.com/opentracing-contrib/python-redis).

Installation
============

Run the following command:

```
$ pip install AIORedis-Opentracing
```

Getting started
===============

Tracing a AIORedis client requires calling ``init_tracing()`` and optionally specify an OpenTracing-compatible tracer.

```python
import aioredis
import aioredis_opentracing

# If not provided, opentracing.tracer will be used.
aioredis_opentracing.init_tracing(tracer)

redis = await aioredis.create_redis_pool('redis://localhost')
await redis.set('last_access', datetime.datetime.now())
```

It's possible to trace only specific pipelines:

```python
aioredis_opentracing.init_tracing(tracer)

pipe = redis.multi_exec()
aioredis_opentracing.trace_pipeline(pipe)

# This pipeline will be executed as a single MULTI command.
pipe.set('key1', 'value1')
pipe.set('key2', 'value2')
ok1, ok2 = await pipe.execute()
```

When pipeline commands are executed as a transaction, these commands will be grouped under a single ``MULTI`` operation. They'll also appear as a single operation in the trace. Outside of a transaction, each command will generate a span.
