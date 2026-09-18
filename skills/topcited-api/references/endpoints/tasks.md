<!-- Generated from the TopCited OpenAPI schema. Do not edit by hand. -->


# tasks

### GET /api/v1/tasks

List Tasks

List tasks for the authenticated customer.

Parameters:
- `task_type` in query
- `status` in query
- `skip` in query
- `limit` in query

Responses: 200, 422

### GET /api/v1/tasks/{task_id}

Get Task

Get a single task by ID.

Parameters:
- `task_id` in path (required)

Responses: 200, 422
