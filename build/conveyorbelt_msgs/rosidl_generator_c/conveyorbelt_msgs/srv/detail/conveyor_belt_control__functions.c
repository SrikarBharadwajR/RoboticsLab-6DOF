// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from conveyorbelt_msgs:srv/ConveyorBeltControl.idl
// generated code does not contain a copyright notice
#include "conveyorbelt_msgs/srv/detail/conveyor_belt_control__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__init(conveyorbelt_msgs__srv__ConveyorBeltControl_Request * msg)
{
  if (!msg) {
    return false;
  }
  // power
  return true;
}

void
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__fini(conveyorbelt_msgs__srv__ConveyorBeltControl_Request * msg)
{
  if (!msg) {
    return;
  }
  // power
}

bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__are_equal(const conveyorbelt_msgs__srv__ConveyorBeltControl_Request * lhs, const conveyorbelt_msgs__srv__ConveyorBeltControl_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // power
  if (lhs->power != rhs->power) {
    return false;
  }
  return true;
}

bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__copy(
  const conveyorbelt_msgs__srv__ConveyorBeltControl_Request * input,
  conveyorbelt_msgs__srv__ConveyorBeltControl_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // power
  output->power = input->power;
  return true;
}

conveyorbelt_msgs__srv__ConveyorBeltControl_Request *
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  conveyorbelt_msgs__srv__ConveyorBeltControl_Request * msg = (conveyorbelt_msgs__srv__ConveyorBeltControl_Request *)allocator.allocate(sizeof(conveyorbelt_msgs__srv__ConveyorBeltControl_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(conveyorbelt_msgs__srv__ConveyorBeltControl_Request));
  bool success = conveyorbelt_msgs__srv__ConveyorBeltControl_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__destroy(conveyorbelt_msgs__srv__ConveyorBeltControl_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    conveyorbelt_msgs__srv__ConveyorBeltControl_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence__init(conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  conveyorbelt_msgs__srv__ConveyorBeltControl_Request * data = NULL;

  if (size) {
    data = (conveyorbelt_msgs__srv__ConveyorBeltControl_Request *)allocator.zero_allocate(size, sizeof(conveyorbelt_msgs__srv__ConveyorBeltControl_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = conveyorbelt_msgs__srv__ConveyorBeltControl_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        conveyorbelt_msgs__srv__ConveyorBeltControl_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence__fini(conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      conveyorbelt_msgs__srv__ConveyorBeltControl_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence *
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence * array = (conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence *)allocator.allocate(sizeof(conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence__destroy(conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence__are_equal(const conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence * lhs, const conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!conveyorbelt_msgs__srv__ConveyorBeltControl_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence__copy(
  const conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence * input,
  conveyorbelt_msgs__srv__ConveyorBeltControl_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(conveyorbelt_msgs__srv__ConveyorBeltControl_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    conveyorbelt_msgs__srv__ConveyorBeltControl_Request * data =
      (conveyorbelt_msgs__srv__ConveyorBeltControl_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!conveyorbelt_msgs__srv__ConveyorBeltControl_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          conveyorbelt_msgs__srv__ConveyorBeltControl_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!conveyorbelt_msgs__srv__ConveyorBeltControl_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__init(conveyorbelt_msgs__srv__ConveyorBeltControl_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__fini(conveyorbelt_msgs__srv__ConveyorBeltControl_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__are_equal(const conveyorbelt_msgs__srv__ConveyorBeltControl_Response * lhs, const conveyorbelt_msgs__srv__ConveyorBeltControl_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__copy(
  const conveyorbelt_msgs__srv__ConveyorBeltControl_Response * input,
  conveyorbelt_msgs__srv__ConveyorBeltControl_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

conveyorbelt_msgs__srv__ConveyorBeltControl_Response *
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  conveyorbelt_msgs__srv__ConveyorBeltControl_Response * msg = (conveyorbelt_msgs__srv__ConveyorBeltControl_Response *)allocator.allocate(sizeof(conveyorbelt_msgs__srv__ConveyorBeltControl_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(conveyorbelt_msgs__srv__ConveyorBeltControl_Response));
  bool success = conveyorbelt_msgs__srv__ConveyorBeltControl_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__destroy(conveyorbelt_msgs__srv__ConveyorBeltControl_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    conveyorbelt_msgs__srv__ConveyorBeltControl_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence__init(conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  conveyorbelt_msgs__srv__ConveyorBeltControl_Response * data = NULL;

  if (size) {
    data = (conveyorbelt_msgs__srv__ConveyorBeltControl_Response *)allocator.zero_allocate(size, sizeof(conveyorbelt_msgs__srv__ConveyorBeltControl_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = conveyorbelt_msgs__srv__ConveyorBeltControl_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        conveyorbelt_msgs__srv__ConveyorBeltControl_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence__fini(conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      conveyorbelt_msgs__srv__ConveyorBeltControl_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence *
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence * array = (conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence *)allocator.allocate(sizeof(conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence__destroy(conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence__are_equal(const conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence * lhs, const conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!conveyorbelt_msgs__srv__ConveyorBeltControl_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence__copy(
  const conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence * input,
  conveyorbelt_msgs__srv__ConveyorBeltControl_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(conveyorbelt_msgs__srv__ConveyorBeltControl_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    conveyorbelt_msgs__srv__ConveyorBeltControl_Response * data =
      (conveyorbelt_msgs__srv__ConveyorBeltControl_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!conveyorbelt_msgs__srv__ConveyorBeltControl_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          conveyorbelt_msgs__srv__ConveyorBeltControl_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!conveyorbelt_msgs__srv__ConveyorBeltControl_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
