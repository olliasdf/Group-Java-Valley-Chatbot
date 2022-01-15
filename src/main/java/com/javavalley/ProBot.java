package com.javavalley;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

import opennlp.tools.doccat.BagOfWordsFeatureGenerator;
import opennlp.tools.doccat.DoccatFactory;
import opennlp.tools.doccat.DoccatModel;
import opennlp.tools.doccat.DocumentCategorizerME;
import opennlp.tools.doccat.DocumentSample;
import opennlp.tools.doccat.DocumentSampleStream;
import opennlp.tools.doccat.FeatureGenerator;
import opennlp.tools.lemmatizer.LemmatizerME;
import opennlp.tools.lemmatizer.LemmatizerModel;
import opennlp.tools.postag.POSModel;
import opennlp.tools.postag.POSTaggerME;
import opennlp.tools.sentdetect.SentenceDetectorME;
import opennlp.tools.sentdetect.SentenceModel;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;
import opennlp.tools.util.InputStreamFactory;
import opennlp.tools.util.InvalidFormatException;
import opennlp.tools.util.MarkableFileInputStreamFactory;
import opennlp.tools.util.ObjectStream;
import opennlp.tools.util.PlainTextByLineStream;
import opennlp.tools.util.TrainingParameters;
import opennlp.tools.util.model.ModelUtil;


public class ProBot {
	static StringSimilarity a = new StringSimilarity();
	private static Map<String, String> questionAnswer = new HashMap<>();
	
	/*
	 * Define answers for each given category.
	 */
	static {
		questionAnswer.put("greeting", "Hello, how can I help you?");
		questionAnswer.put("conversation-continue", "What else can I help you with?");
		questionAnswer.put("conversation-complete", "Nice chatting with you. Bye!");
		questionAnswer.put("question", "this is a test");

	}

	public static void main(String[] args) throws FileNotFoundException, IOException, InterruptedException {
		
		
		// Train categorizer model to the training data we created.
		DoccatModel model = trainCategorizerModel();

		// Take chat inputs from console (user) in a loop.
		Scanner scanner = new Scanner(System.in);
		while (true) {

			// Get chat input from user.
			System.out.println("You:");
			String userInput = scanner.nextLine();
			
			// Break users chat input into sentences using sentence detection.
			String[] sentences = breakSentences(userInput);

			String answer = "";
			boolean conversationComplete = false;

			// Loop through sentences.
			for (String sentence : sentences) {

				// Separate words from each sentence using tokenizer.
				String[] tokens = tokenizeSentence(sentence);

				// Tag separated words with POS tags to understand their grammatical structure.
				String[] posTags = detectPOSTags(tokens);

				// Lemmatize each word so that its easy to categorize.
				String[] lemmas = lemmatizeTokens(tokens, posTags);

				// Determine BEST category using lemmatized tokens using the model that we trained
				// at start.
				String category = detectCategory(model, lemmas);
				
				// Get predefined answer from given category & add to answer.
				answer = answer + " " + questionAnswer.get(category);

				// If category conversation-complete, we will end chat conversation.
				if ("conversation-complete".equals(category)) {
					conversationComplete = true;
				}
			}

			// Print answer back to user. If conversation is marked as complete, then end
			// loop & program.
			System.out.println("ProBot: " + answer);
			
			if (conversationComplete) {
				break;
			}

		}

	}

	/**
	 * Train categorizer model as per the category sample training data we created.
	 * 
	 * @return
	 * @throws FileNotFoundException
	 * @throws IOException
	 */
	private static DoccatModel trainCategorizerModel() throws FileNotFoundException, IOException {
		// faq-categorizer.txt is a custom training data with categories as per our chat
		// requirements.
		InputStreamFactory inputStreamFactory = new MarkableFileInputStreamFactory(new File("faq-categorizer.txt"));
		ObjectStream<String> lineStream = new PlainTextByLineStream(inputStreamFactory, StandardCharsets.UTF_8);
		ObjectStream<DocumentSample> sampleStream = new DocumentSampleStream(lineStream);

		DoccatFactory factory = new DoccatFactory(new FeatureGenerator[] { new BagOfWordsFeatureGenerator() });

		TrainingParameters params = ModelUtil.createDefaultTrainingParameters();
		params.put(TrainingParameters.CUTOFF_PARAM, 0);

		// Train a model with classifications from above file.
		DoccatModel model = DocumentCategorizerME.train("en", sampleStream, params, factory);
		return model;
	}

	/**
	 * Detect category using given token. Use categorizer feature of Apache OpenNLP.
	 * 
	 * @param model
	 * @param finalTokens
	 * @return
	 * @throws IOException
	 */
	private static String detectCategory(DoccatModel model, String[] finalTokens) throws IOException {

		// Initialize document categorizer tool
		DocumentCategorizerME myCategorizer = new DocumentCategorizerME(model);

		// Get best possible category.
		double[] probabilitiesOfOutcomes = myCategorizer.categorize(finalTokens);
		String category = myCategorizer.getBestCategory(probabilitiesOfOutcomes);
		
		
		
		
		System.out.println("Category: " + category);
		System.out.println("question".equals(category));
		
		
		
		
		return category;

	}

	/**
	 * Break data into sentences using sentence detection feature of Apache OpenNLP.
	 * 
	 * @param data
	 * @return
	 * @throws FileNotFoundException
	 * @throws IOException
	 */
	private static String[] breakSentences(String data) throws FileNotFoundException, IOException {
		// Better to read file once at start of program & store model in instance
		// variable. but keeping here for simplicity in understanding.
		try (InputStream modelIn = new FileInputStream("en-sent.bin")) {

			SentenceDetectorME myCategorizer = new SentenceDetectorME(new SentenceModel(modelIn));

			String[] sentences = myCategorizer.sentDetect(data);
			System.out.println("Sentence Detection: " + Arrays.stream(sentences).collect(Collectors.joining(" | ")));

			return sentences;
		}
	}

	/**
	 * Break sentence into words & punctuation marks using tokenizer feature of
	 * Apache OpenNLP.
	 * 
	 * @param sentence
	 * @return
	 * @throws FileNotFoundException
	 * @throws IOException
	 */
	private static String[] tokenizeSentence(String sentence) throws FileNotFoundException, IOException {
		// Better to read file once at start of program & store model in instance
		// variable. but keeping here for simplicity in understanding.
		try (InputStream modelIn = new FileInputStream("en-token.bin")) {

			// Initialize tokenizer tool
			TokenizerME myCategorizer = new TokenizerME(new TokenizerModel(modelIn));

			// Tokenize sentence.
			String[] tokens = myCategorizer.tokenize(sentence);
			System.out.println("Tokenizer : " + Arrays.stream(tokens).collect(Collectors.joining(" | ")));

			return tokens;

		}
	}

	/**
	 * Find part-of-speech or POS tags of all tokens using POS tagger feature of
	 * Apache OpenNLP.
	 * 
	 * @param tokens
	 * @return
	 * @throws IOException
	 */
	private static String[] detectPOSTags(String[] tokens) throws IOException {
		// Better to read file once at start of program & store model in instance
		// variable. but keeping here for simplicity in understanding.
		
	
		try (InputStream modelIn = new FileInputStream("en-pos-maxent.bin")) {

			// Initialize POS tagger tool
			POSTaggerME myCategorizer = new POSTaggerME(new POSModel(modelIn));

			// Tag sentence.
			String[] posTokens = myCategorizer.tag(tokens);
			System.out.println("POS Tags : " + Arrays.stream(posTokens).collect(Collectors.joining(" | ")));
			
			return posTokens;

		}

	}

	/**
	 * Custom function for extracting nouns from user queries.
	 */
	
	public static ArrayList<String> getNoun (String[] tokens, String[] posTags) {
		
		ArrayList<String> nouns = new ArrayList<String>();
		for (int i = 0 ; i < posTags.length ; i++) {
			
			if(posTags[i].equals("NNP" ) || posTags[i].equals("NN" )  || posTags[i].equals("NNS"  )) {
				
				nouns.add(tokens[i]);
			}
		}
		
		return nouns;
	}
		
	/**
	 * Custom function for detecting topics from user queries.
	 */
	
	
	public static String detectTopic (ArrayList<String> nouns) {
		
		String topics = "";
		BufferedReader reader;
		try {
			double j = 0;
			double save = 0;
			
			String helpnoun = "";
			
			for (String b : nouns) {
			helpnoun += " " +  b;
			}
			String helpnoun2 = helpnoun.toLowerCase();
			StringSimilarity x = new StringSimilarity();
			reader = new BufferedReader(new FileReader(
					System.getProperty("user.dir") + "\\src\\main\\java\\com\\javavalley\\" + "Wikipedia_topics"));
			String line = reader.readLine();
			while (line != null) {
				
				
				for (String a : nouns) {
					
					String saver = line.toLowerCase();
					
				if (saver.contains(a.toLowerCase())) {
					
					j = x.similarity(helpnoun, saver);
					
					if (j > save) {
						System.out.println(line);
						topics = line;
						save = j;
					}
					else { if (j == save)
					{		
						
					     if (x.similarity(helpnoun, line) > x.similarity(helpnoun, topics)) {
					    	
								topics = line;
								save = j; 
					    	 
					    	 
					     }
						
					}
					}
				// read next line
				}
				
			}
				line = reader.readLine();	
			}
			
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
			System.out.println("Topic Not Found");
			
		}
		
		return topics;
		
		
	}
	
	/**
	 * Find lemma of tokens using lemmatizer feature of Apache OpenNLP.
	 * 
	 * @param tokens
	 * @param posTags
	 * @return
	 * @throws InvalidFormatException
	 * @throws IOException
	 */
	
	private static String[] lemmatizeTokens(String[] tokens, String[] posTags)
			throws InvalidFormatException, IOException {
		// Better to read file once at start of program & store model in instance
		// variable. but keeping here for simplicity in understanding.
		try (InputStream modelIn = new FileInputStream("en-lemmatizer.bin")) {

			// Tag sentence.
			LemmatizerME myCategorizer = new LemmatizerME(new LemmatizerModel(modelIn));
			String[] lemmaTokens = myCategorizer.lemmatize(tokens, posTags);
			System.out.println("Lemmatizer : " + Arrays.stream(lemmaTokens).collect(Collectors.joining(" | ")));

			return lemmaTokens;

		}
	}
	
	
	/**
	 * Custom function for detecting topics from user queries.
	 */
	
	public static ArrayList<String> findNouns (String text) throws IOException{
		
		
		String [] tokens = tokenizeSentence(text);
		String [] posTags = detectPOSTags(tokens);
		Boolean b = false;
		ArrayList<String> nouns = getNoun(tokens,posTags);
		
		ArrayList<String> topics = new ArrayList<String>();
		BufferedReader reader;
		try {
			
			
			
			reader = new BufferedReader(new FileReader(
					System.getProperty("user.dir") + "\\src\\main\\java\\com\\javavalley\\" + "Wikipedia_topics"));
			String line = reader.readLine();
			while (line != null) {
				
				
				for (String a : nouns) {
					
					String saver = line.toLowerCase();
					
				if (saver.contains(a.toLowerCase())) {

					
				// read next line
				}else {
					b = false;
				}
				
			}
				if(nouns.size() == 1) {
				if (b && line.length() < 14) {
					
					  topics.add(line);
				}
				}
					  else {
						  if (b) {
								
							  topics.add(line);
			}
						  }
				
				
				line = reader.readLine();	
				b = true;
			
		} 
			reader.close();	
		}catch (IOException e) {
			e.printStackTrace();
			System.out.println("Noun not found!");
			
		}
				
		return topics ;

	}
public static ArrayList<String> findNouns2 (String text) throws IOException{
		
		
		String [] tokens = tokenizeSentence(text);
		String [] posTags = detectPOSTags(tokens);
		
		ArrayList<String> nouns = getNoun(tokens,posTags);
		return nouns;
}
	
	public static String findTopic (String text) throws Exception{
		
		
		
		String [] tokens = tokenizeSentence(text);
		String [] posTags = detectPOSTags(tokens);
		
		ArrayList<String> nouns = getNoun(tokens,posTags);
		
		
		String output = detectTopic(nouns);
		return output;

	}

	public static String findCategory(String text) throws Exception {
		String [] sents = breakSentences(text);
		
		String [] tokens = tokenizeSentence(text);
		
		String [] posTags = detectPOSTags(tokens);
		
		String [] lemmas = lemmatizeTokens(tokens, posTags);
		
		DoccatModel model = trainCategorizerModel();
		
		String category = detectCategory(model, lemmas);
		
		return category;
	}
}
