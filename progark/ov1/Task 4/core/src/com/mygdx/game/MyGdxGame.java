package com.mygdx.game;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.GlyphLayout;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.glutils.ShapeRenderer;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.FitViewport;

import java.util.Locale;
import java.util.concurrent.TimeUnit;

public class MyGdxGame extends ApplicationAdapter {
    private Stage stage;
    private OrthographicCamera cam;
    private SpriteBatch batch;
    private BitmapFont font;
    private static GlyphLayout glyphLayout;
    private Paddle paddle1;
    private Paddle paddle2;
    private Ball ball;
    private int score1 = 0;
    private int score2 = 0;

    @Override
    public void create() {
        cam = new OrthographicCamera();
        batch = new SpriteBatch();
        font = new BitmapFont();
        glyphLayout = new GlyphLayout();

        FitViewport viewport = new FitViewport(Gdx.graphics.getWidth(), Gdx.graphics.getHeight(), cam);
        stage = new Stage(viewport, batch);
        Gdx.input.setInputProcessor(stage);

        font.setColor(Color.WHITE);
        font.getData().setScale(2.5f);

        paddle1 = new Paddle(10, Gdx.graphics.getHeight() / 2 - 150, 40, 300);
        paddle2 = new Paddle(Gdx.graphics.getWidth() - 50, Gdx.graphics.getHeight() / 2 - 150, 40, 300, true);
        ball = new Ball(40, 40);

        stage.addActor(paddle1);
        stage.addActor(paddle2);
        stage.addActor(ball);
    }

    @Override
    public void render() {
        ScreenUtils.clear(0.1f, 0.4f, 0.2f, 1);

        if (score1 < 21 && score2 < 21) {
            float delta = Gdx.graphics.getDeltaTime();

            if (paddle1.isAi()) {
                paddle1.aiMovement(delta, ball.getYPos() + (ball.getHeight() / 2));
            }

            if (paddle2.isAi()) {
                paddle2.aiMovement(delta, ball.getYPos() + (ball.getHeight() / 2));
            }

            if (ball.getNextHitbox(delta).overlaps(paddle1.getHitbox()) || ball.getNextHitbox(delta).overlaps(paddle2.getHitbox())) {
                ball.flipXDirection();
            }

            if (ball.getXPos() >= Gdx.graphics.getWidth()) {
                score1 += 1;
                resetPositions();
            }

            if (ball.getXPos() <= 0) {
                score2 += 1;
                resetPositions();
            }

            batch.begin();
            glyphLayout.setText(font, String.format(Locale.UK, "%d : %d", score1, score2));
            font.draw(batch, glyphLayout, Gdx.graphics.getWidth() / 2 - glyphLayout.width / 2, Gdx.graphics.getHeight() - 50);
            batch.end();

            stage.act(delta);
            stage.draw();
        } else {
            String winner = score1 == 21 ? "Player 1" : "Player 2";
            batch.begin();
            glyphLayout.setText(font, String.format(Locale.UK, "%s wins!! Press here to restart.", winner));
            font.getData().setScale(5f);
            font.draw(batch, glyphLayout, Gdx.graphics.getWidth() / 2 - glyphLayout.width / 2, Gdx.graphics.getHeight() / 2);
            batch.end();

            Rectangle textBox = new Rectangle(Gdx.graphics.getWidth() / 2 - glyphLayout.width / 2, Gdx.graphics.getHeight() / 2, glyphLayout.width, glyphLayout.height);

            if (Gdx.input.isTouched() && textBox.contains(Gdx.input.getX(), Gdx.input.getY())) {
                score1 = 0;
                score2 = 0;
                font.getData().setScale(2.5f);
            }
        }
    }

    @Override
    public void dispose() {
        stage.dispose();
        batch.dispose();
    }

    public void resetPositions() {
        setPaddleMods(1);
        ball.setGoStraightMod(1);
        ball.resetGame();
        paddle1.setPosition(10, Gdx.graphics.getHeight() / 2 - 150);
        paddle2.setPosition(Gdx.graphics.getWidth() - 50, Gdx.graphics.getHeight() / 2 - 150);
    }

    public void setPaddleMods(int mod) {
        paddle1.setMoveDownMod(mod);
        paddle1.setMoveUpMod(mod);
        paddle1.setMoveDownMod(mod);
        paddle2.setMoveUpMod(mod);
    }
}
