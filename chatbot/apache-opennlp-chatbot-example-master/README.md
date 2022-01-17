# `Text Retrieval Chatbot`

To implement a chatbot based text search engine with GUI. The backend will index the documents in Apache Lucene/Solr. Making simple assumptions that in the front-end user can ask questions like “why” and “how”. For other queries (i.e. non-who and non-how queries), we resort to simple free text search and query Lucene/Solr. Making simple and reasonable assumptions, like restricting the number of results to 3 or 5 or also get images along with text or ask feedback from the user in the GUI! As a final result, we expect a GUI where user can search in a "chat like experience".

## `Abstract`

We plan to create an automated chat agent "Topic Explainer" that is designed for querying files present in the system. The files that we are using for this use case is only text files. User will ask the bot is expected to reply with greetings, answers to questions about content present in the files etc. We have a sample search space as text files for implementing this use case. We built a GUI in Java Swing to have a chat-like experience. We will ask questions in a different way for various topics.

**Chatbot API**: Apache OpenNLP (1.5 series)

### About OpenNLP API

Apache **OpenNLP** is an open-source Java library which is used to pre-process natural language text. OpenNLP offers services such as tokenization, sentence segmentation, part-of-speech tagging, named entity extraction, chunking, parsing etc.

- We will use seldom trained models for our work from <http://opennlp.sourceforge.net/models-1.5/>

- We take some motivation from Natural Language Processing (NLP) to perform this task. A rough pipeline of our chatbot working are as follows:

  - Trains *categorizer* model with latest samples data (a text file as training data contains user queries for interaction with bot).
  - Take input from the user.
  - Partition the sentences.
  - Tokenize each sentences into words.
  - Find POS tags for each word (for next step).
  - Lemmatize each word using tokens & POS tags. This will make it very easy to put in categories as we do not have to have all lemma possibilities in categorizer samples data.
  - Categorize lemma tokens & then find answer for detected category.

To keep the chat simple we define the below categories:

*greeting* - Basic greetings that we anticipate user to use to start chat.

*conversation-continue* - Words like “ok”, “hmm” that user might use in between of conversation.

*conversation-complete* - Words or sentences that user might end to end conversation.

*question* -  Questions that user will ask questions in a different way for various topics.

In total we used 4 trained NLP models from Apache OpenNLP (`en-sent.bin`, `en-token.bin`, `en-pos-maxent.bin`, `en-lemmatizer.bin`)

### Technical Specifications

- Tested on Windows 10 (Home), Windows 11
- Requires Java 1.8 (JRE System Library [JavaSE-1.8])

### Running this project (User Guide)

- Step 1: Unzip the uploaded file from Moodle.
- Step 2: Open a code editor (VS Code or Eclispe).
- Step 3: Run this file from the directory where it resides. The `ProBot.java` runs in the console (background).
- Step 4: Run the `ChatBotUI.java` for a GUI, by or by right-clicking the file from Eclipse project. And it should pop-up a UI in the foreground. 

### Observed output of our program

![](https://github.com/olliasdf/Group-Java-Valley-Chatbot/blob/main/IR-P05.jpg)

## Related References

[1] <https://opennlp.apache.org/models.html>

[2] <http://opennlp.sourceforge.net/models-1.5/>

[3] <https://opennlp.apache.org/docs/1.8.1/manual/opennlp.html>

[4] <https://self-learning-java-tutorial.blogspot.com/2015/10/opennlp-tokenization.html>

[5] <https://www.tutorialspoint.com/opennlp/opennlp_quick_guide.htm>

[6] <https://raw.githubusercontent.com/richardwilly98/elasticsearch-opennlp-auto-tagging/master/src/main/resources/models/en-lemmatizer.dict>

[7] <http://www.java2s.com/example/java-api/opennlp/tools/util/trainingparameters/cutoff_param-0.html>

[8] <http://www.java2s.com/example/java-src/pkg/opennlp/tools/util/trainingparameters-98536.html>

[9] <https://programtalk.com/java-api-usage-examples/opennlp.tools.util.TrainingParameters/>

[10] <https://www.guru99.com/java-swing-gui.html>

[11] <https://docs.oracle.com/javase/tutorial/uiswing/index.html>

