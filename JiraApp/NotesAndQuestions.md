
# Unresolved

## 1. How do we know when we have reached a ticket that we have processed before?

We should probably just process all of the tickets that have not yet been finished.

## 3. How do we know when new test cases have been added to the tickets?

Thought: we might be able to keep track of the last document, run the process for all open JIRA tickets, and compare the old to the new. We only would include the new ones.

OR 

We can just run the job every time for all JIRA tickets so that we always have the most up-to-date version of tests.

