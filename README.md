# `Problem Statement`

To implement a chatbot based text search engine with GUI. The backend will index
the documents in Apache Lucene/Solr. Making simple assumptions that in the front-end user can ask questions
like “why” and “how”. For other queries (i.e. non-who and non-how queries), we
resort to simple free text search and query Lucene/Solr. Making simple and
reasonable assumptions, like restricting the number of results to 3 or 5 or also get images
along with text or ask feedback from the user in the GUI! As a final result, we expect a
GUI where user can search in a "chat like experience".


# `Abstract`

We plan to create an automated chat agent that is designed for querying files present in the system. The files that we are using for this use case is only text files. User will ask the bot is expected to reply with greetings, answers to questions about content present in the files etc. We have a sample search space as text files for implementing this use case. We built a GUI in Java Swing to have a chat-like experience.
