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

    private static final int COIN_COUNT = 2;
    private static int[] coinX = new int[COIN_COUNT];
    private static int[] coinY = new int[COIN_COUNT];
    private static int[] coinVelocity = new int[COIN_COUNT];
    private static int gravity = 1;
    private static int jumpStrength = -20;
    private static Image[] coinImage = new Image[COIN_COUNT];

    public static void main(String[] args) {
        SwingUtilities.invokeLater(CoinFlipAnimation::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Coin Flip");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(900, 500);

        // Coin 1 starts immediately
        startAnimation(0, frame);

        // Coin 2 starts after a delay of 1 second
        Timer delayTimer = new Timer(1000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                startAnimation(1, frame);
                ((Timer) e.getSource()).stop();
            }
        });
        delayTimer.setRepeats(false);
        delayTimer.start();

        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                drawCoinFlip((Graphics2D) g);
            }
        };
        frame.add(panel);

        frame.setVisible(true);

        // Schedule task to close the JFrame after 5 seconds
        Timer closeTimer = new Timer(5000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose(); // Close the JFrame
            }
        });
        closeTimer.setRepeats(false);
        closeTimer.start();
    }

    private static void startAnimation(int coinIndex, JFrame frame) {
        coinX[coinIndex] = (WIDTH / 2) - (IMAGE_WIDTH / 2) + ((coinIndex == 0) ? -100 : 100);
        coinY[coinIndex] = (HEIGHT - IMAGE_HEIGHT) / 2;
        coinVelocity[coinIndex] = 0;
        coinImage[coinIndex] = HEADS_IMAGE;

        Timer timer = new Timer(30, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                coinVelocity[coinIndex] += gravity;
                coinY[coinIndex] += coinVelocity[coinIndex];

                if (coinY[coinIndex] >= HEIGHT - IMAGE_HEIGHT) {
                    coinY[coinIndex] = HEIGHT - IMAGE_HEIGHT;
                    coinVelocity[coinIndex] = jumpStrength;

                    // Toggle the coin image between heads and tails
                    coinImage[coinIndex] = (coinImage[coinIndex] == HEADS_IMAGE) ? TAILS_IMAGE : HEADS_IMAGE;
                }

                frame.repaint();
            }
        });
        timer.start();
    }

    private static void drawCoinFlip(Graphics2D g) {
        g.setColor(new Color(0xB7521E));
        g.fillRect(0, 0, WIDTH, HEIGHT);
        for (int i = 0; i < COIN_COUNT; i++) {
            g.drawImage(coinImage[i], coinX[i], coinY[i], IMAGE_WIDTH, IMAGE_HEIGHT, null);
        }
    }
}
