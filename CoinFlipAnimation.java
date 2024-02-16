import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CoinFlipAnimation {

    // Dimensions
    private static final int WIDTH = 900;
    private static final int HEIGHT = 500;

    // Load image files
    private static final Image HEADS_IMAGE = Toolkit.getDefaultToolkit().getImage("heads_coin.png");
    private static final Image TAILS_IMAGE = Toolkit.getDefaultToolkit().getImage("tails_coin.png");
    private static final int IMAGE_WIDTH = 100;
    private static final int IMAGE_HEIGHT = 100;

    private static int coinX = (WIDTH - IMAGE_WIDTH) / 2;
    private static int coinY = (HEIGHT - IMAGE_HEIGHT) / 2;
    private static int coinVelocity = 0;
    private static int gravity = 1;
    private static int jumpStrength = -20;
    private static Image coinImage = HEADS_IMAGE;
    private static int frames = 200; // Increased number of frames

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> createAndShowGUI());
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Coin Flip");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(900, 500);
        

        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                drawCoinFlip((Graphics2D) g);
            }
        };
        frame.add(panel);

        frame.setVisible(true);

        Timer timer = new Timer(30, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (frames > 1) {
                    coinVelocity += gravity;
                    coinY += coinVelocity;

                    if (coinY >= HEIGHT - IMAGE_HEIGHT) {
                        coinY = HEIGHT - IMAGE_HEIGHT;
                        coinVelocity = jumpStrength;

                        // Toggle the coin image between heads and tails
                        coinImage = (coinImage == HEADS_IMAGE) ? TAILS_IMAGE : HEADS_IMAGE;
                    }
                } else {
                    ((Timer) e.getSource()).stop();
                }

                frames--;
                frame.repaint();
            }
        });
        timer.start();
    }

    private static void drawCoinFlip(Graphics2D g) {
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, WIDTH, HEIGHT);
        g.drawImage(coinImage, coinX, coinY, IMAGE_WIDTH, IMAGE_HEIGHT, null);
    }
}
