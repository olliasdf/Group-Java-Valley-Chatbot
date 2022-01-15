package com.javavalley;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JScrollPane;

import java.awt.event.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

import javax.swing.border.Border;
import javax.swing.BorderFactory;
import java.lang.Override;
import java.lang.Thread;
import java.awt.*;
import javax.swing.*;
import javax.swing.border.*;
import java.lang.Math;

public class ChatBot extends JFrame{
	
	private JFrame frame;
	private JTextArea chatArea;
	private JTextField chatBox;
	private JScrollPane scroll;
	private Border border;
	
	
	public static void main(String[] args){
		new ChatBot();
	}
	
	public ChatBot(){
		
		String topic = "";
		JPanel gui = new JPanel(new BorderLayout(5,5));
		JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());
        frame = new JFrame("Topic Explainer");
        frame.setContentPane(gui);
        chatArea = new JTextArea(10, 50);
        chatBox = new JTextField();
        scroll = new JScrollPane(chatArea,
                JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,
                JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
        border = BorderFactory.createLineBorder(Color.BLUE, 1);
        chatBox.setBorder(border);

        JLabel bot = new JLabel(
                "Hello! I can answer topic-related queries! " +
                "Ask me by typing above. Type \"q\" to end the program.");
        chatArea.append("Chats: \n");
        chatBox.setText("");

        gui.add(chatBox, BorderLayout.PAGE_START);
        gui.add(scroll);
        gui.add(bot, BorderLayout.PAGE_END);
        gui.setBorder(new EmptyBorder(5,5,5,5));
        frame.setResizable(false);
        frame.pack();
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        chatBox.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				String gtext = chatBox.getText();
				chatArea.append("You: " +gtext + "\n");
				chatBox.setText("");
				if(gtext.equals("Q")|gtext.equals("q")|gtext.equals("exit")) {
					sleep(500);
					System.exit(0);
				}
				String category = "";
				try {
						category = ProBot.findCategory(gtext);
						System.out.println(category);
				}
				catch (Exception e) {
					System.out.println("Exception thrown.");
				}
				
				
				if ((category.equals("question"))) {
				
					
			
					try {
						
						String topicsaver = ProBot.findTopic(gtext).toLowerCase();
						System.out.println(topicsaver);
						System.out.println(System.getProperty("user.dir") + "\\PythonScript\\TextFiles\\" + topicsaver + ".txt" );
						BufferedReader br = new BufferedReader(new FileReader(System.getProperty("user.dir") + "\\PythonScript\\TextFiles\\" + topicsaver + ".txt" ));
						
						
						bot(readAllLines(br));
						
						
							
						
				} catch (Exception e) {
					
					e.printStackTrace();
					System.out.println("Topic Not Found");
				}
					
					
				}else {
				String response = respond(category);
				bot(response);
				}
				}
			});	
        
	}
		
	
	public String readAllLines(BufferedReader reader) throws IOException {
	    StringBuilder content = new StringBuilder();
	    String line;
	    
	    while ((line = reader.readLine()) != null) {
	        content.append(line);
	        content.append(System.lineSeparator());
	    }

	    return content.toString();
	}
		private void bot(String string)
		{
			chatArea.append("Bot: " + string + "\n");
		}
		
		
		private void sleep(int x) {
			try {
				Thread.sleep(x);
			} catch (InterruptedException e) {
				e.printStackTrace();
				
			}
		}
		
		private String respond(String category)
		{
			String[] greetings = {"Hello, how can I help you?"};
			String[] conversationComplete = {"Goodbye", "Bye", "Nice chatting with you. Bye!"};
			
			if (category.equals("greeting")) return greetings[(int) (Math.random()*greetings.length)];
			else if (category.equals("conversation-complete")) return conversationComplete[(int) (Math.random()*conversationComplete.length)];
			else return "Err.. :( Sorry, I did'nt get that!";
 		}
		
}