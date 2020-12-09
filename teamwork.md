# Teamwork - Iteration 3
Reflect on your use of agile practices and how you worked as a team.

Iteration 3 has gone smoothly since we've reflected on our teamwork strategies in iterations 1 and 2, and improved our use of agile practices from feedback given.

###    How often you met, and why you met that often

Since our teamwork practices from iteration 2 were quite successful and we were satisfied with our progress, the workload felt a lot lighter overall. Hence, our group mutually agreed that it wasn't necessary to meet in person as often in iteration 3. 

Throughout iteration 3, we got together in person two times to hold standups and help eachother, mainly through pair programming. At the end of each meeting, we ensured that each team member would let the group know which tasks they would get done by the next meeting. This was to ensure each member was held accountable and understood the work they had to do, and so we'd have a clear idea of our overall progress for the iteration. Our method of communicating online was via Slack, where we would confirm our meeting times/places in accordance with group members' availabilities. 

Overall, meetings in person and online throughout iteration 3 were largely successful as they allowed us to resolve misunderstandings and other issues (e.g. code-based errors) in a timely manner, and also allowed us to stay focused and with clear objectives throughout the iteration.

###    What methods you used to ensure that meetings were successful

In a similar fashion to iteration 1 and 2, at the beginning of each meeting we would hold a standup to ensure that every team member was on the same page in terms of knowledge about our overall progress. Additionally, it allowed team members to let each other know if they were struggling with any facet of the iteration which allowed us to be more transparent and team-focused.

As a flow-based approach for development in iteration 2 worked well for us, we decided to utilise this agile practice again for iteration 3. We implemented tasks from a queue of to-do items which was based on the iteration 3 specification updates, documentation requirements, and refactoring of our code and test suites.

Our most commonly used software developement method was pair programming (an agile practice originating from extreme programming), where our group worked on testing and refactoring together. This resulted in more robust and higher quality code and documentation, and resolved code-based issues much faster than if we worked individually. 

We also employed "Extreme Programming", an agile practice focused on the values of communication, simplicity, feedback, courage and respect. Extreme programming involves extensive code reviews, unit testing of all code, top-down thinking and ensuring code simplicity/clarity. During meetings, a portion would be dedicated to code review and subsequent pair programming, where all members would state any problems with their code and others would try to help them resolve these issues.

###    What steps you took when things did not go to plan during the iteration

During our iteration 3, time management was a minor issue as we only began implementing changes in the second week of the iteration. Our group members were rather burnt out after iteration 2 and we collectively agreed that taking a short break before starting iteration 3 would boost our productivity and allow us to work better. As a result of the short timespan, a decision was made to work overnight in person to get back on track at the start of week 9. Since our pair programming was such a successful strategy, we agreed to complete some aspects of our code as a tea. During that overnight meeting we finished integrating the backend with the frontend, and then began refactoring our code.

However, upon more comprehensive manual testing with the frontend, we rediscovered issues in user/profiles/uploadphoto, message/(un)pin and message/(un)react. Once more, these issues were raised in our team Slack Workspace, and a meeting was scheduled to fix these bugs through pair programming. Finding the source of these issues was done quickly since we had multiple team members looking for them, and they were resolved either by ourselves, or through getting external help from the Piazza forum.

###    Details on how you had multiple people working on the same code

Similarly to iteration 2, we used git operations such as branching and merge requests, which ensured that multiple people can work on the same code whilst our master branch remains safe from any unexpected errors. If merge conflicts arose, the team members responsible could discuss and reach an agreement more effectively, as merge conflicts can be reviewed through gitlab. 

Furthermore, in order for all group members to stay on the same page and reduce "design smells", we created a file called component/general.py which contained all the helper functions that we would need to access in order to implement the actual functions. This allowed our time to be spent more effectively as group members would not need to repeatedly code the same functions. Commenting played a huge role in this assignment overall, as code style varied between members, so everyone commented their code if necessary, so that anyone could view the code and understand its functionality. 

Additionally, we placed heavy emphasis during the refactoring of our code on having variables and function names that are easy to understand in the scope of their functions/files, further improving our ability to work on the same codebase effectively.

We also decided to draw out a visual representation of our database and what type of data was meant to be in each type field. This was all made accessible to all group members on the slack application, where we would all communicate online all our coding obstacles and further communciate any ambiguities within the assignment specification.

