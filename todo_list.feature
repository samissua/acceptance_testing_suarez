Feature: To-Do List Management
  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When  the user adds a task "Buy groceries" "Buy fruits, vegetables and diary"
    Then the to-do list should contain 1 tasks in total
    And the to-do list should contain:
      | Title         | Description                          |Date        | Status    |
      | Buy groceries | Buy fruits, vegetables and diary     |2025-07-07  | Not Done  |

  Scenario: List all tasks in the to-do list
    Given the to-do list contains:
      | Title         | Description                          |Date        | Status    |
      | Buy groceries | Buy fruits, vegetables and diary     |2025-07-07  | Not Done  |
      | Pay bills     | Pay the electricity and water bills  |2025-07-07  | Not Done  |
    When the user lists all tasks
    Then the to-do list should contain:
      | Title         | Description                          |Date        | Status    |
      | Buy groceries | Buy fruits, vegetables and diary     |2025-07-07  | Not Done  |
      | Pay bills     | Pay the electricity and water bills  |2025-07-07  | Not Done  |

    Scenario: Mark a task as completed
    Given the to-do list contains:
      | Title         | Description                          |Date        | Status    |
      | Buy groceries | Buy fruits, vegetables and diary     |2025-07-07  | Not Done  |
      | Pay bills     | Pay the electricity and water bills  |2025-07-07  | Not Done  |
    When the user marks the task 1 as completed
    Then the to-do list should contain:
      | Title         | Description                          |Date        | Status    |
      | Buy groceries | Buy fruits, vegetables and diary     |2025-07-07  | Done      |
      | Pay bills     | Pay the electricity and water bills  |2025-07-07  | Not Done  |

    Scenario: Clear the entire to-do list
    Given the to-do list contains:
      | Title         | Description                          |Date        | Status    |
      | Buy groceries | Buy fruits, vegetables and diary     |2025-07-07  | Done      |
      | Pay bills     | Pay the electricity and water bills  |2025-07-07  | Not Done  |
    When the user clears the to-do list
    Then the to-do list is empty

    Scenario: Update a task
    Given the to-do list contains:
      | Title         | Description                          |Date        | Status    |
      | Buy groceries | Buy fruits, vegetables and diary     |2025-07-07  | Done      |
      | Pay bills     | Pay the electricity and water bills  |2025-07-07  | Not Done  |
    When the user updates the task 1 to "Buy groceries and meat" "Buy fruits, vegetables, diary and meat"
    Then the to-do list should contain
      | Title                   | Description                                |Date        | Status    |
      | Buy groceries and meat  | Buy fruits, vegetables, diary and meat     |2025-07-07  | Done      |
      | Pay bills               | Pay the electricity and water bills        |2025-07-07  | Not Done  |

  Scenario: Mark a task as not completed
    Given the to-do list contains:
      | Title         | Description                          |Date        | Status    |
      | Buy groceries | Buy fruits, vegetables and diary     |2025-07-07  | Done      |
      | Pay bills     | Pay the electricity and water bills  |2025-07-07  | Not Done  |
    When the user marks the task 1 as not completed
    Then the to-do list should contain
      | Title         | Description                          |Date        | Status    |
      | Buy groceries | Buy fruits, vegetables and diary     |2025-07-07  | Not Done  |
      | Pay bills     | Pay the electricity and water bills  |2025-07-07  | Not Done  |
