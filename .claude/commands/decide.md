Guide the user through pending decisions across Policy Council projects.

First, check all project human_review/ folders:
- projects/economic-prosperity/human_review/
- projects/jobs-guarantee/human_review/

If the user specifies a project, only check that project's folder.

For each pending decision:
1. State which project the decision is for
2. Present the context and background
3. Clearly state what decision is needed
4. Present the options with pros/cons for each
5. Ask for the user's decision
6. After they decide:
   - Log it to that project's DECISION_LOG.md
   - Move the item from human_review/ to the appropriate location
   - Update the project's STATE.json and PROJECT_DASHBOARD.md

If no decisions are pending, inform the user and show what's currently in progress across all projects.
