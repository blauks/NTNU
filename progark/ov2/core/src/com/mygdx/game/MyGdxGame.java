package com.mygdx.game;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.GlyphLayout;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.FitViewport;
import com.mygdx.game.controllers.Controller;

import java.util.Locale;

// View of MVC
public class MyGdxGame extends ApplicationAdapter {
    private Stage stage;
    private OrthographicCamera cam;
    private SpriteBatch batch;
    private BitmapFont font;
    private static GlyphLayout glyphLayout;
    private Controller controller;

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

        controller = new Controller(stage);
    }

    @Override
    public void render() {
        ScreenUtils.clear(0.1f, 0.4f, 0.2f, 1);
        if (controller.getGameUnderway()) {
            batch.begin();
            glyphLayout.setText(font, controller.getScoreboard());
            font.draw(batch, glyphLayout, Gdx.graphics.getWidth() / 2 - glyphLayout.width / 2, Gdx.graphics.getHeight() - 50);
            batch.end();

            controller.render(Gdx.graphics.getDeltaTime());
            stage.draw();
        }
        else {
            batch.begin();
            glyphLayout.setText(font, String.format(Locale.UK, "%s wins!! Press here to restart.", controller.getWinner()));
            font.getData().setScale(5f);
            font.draw(batch, glyphLayout, Gdx.graphics.getWidth() / 2 - glyphLayout.width / 2, Gdx.graphics.getHeight() / 2);
            batch.end();

            Rectangle textBox = new Rectangle(Gdx.graphics.getWidth() / 2 - glyphLayout.width / 2, Gdx.graphics.getHeight() / 2, glyphLayout.width, glyphLayout.height);

            if(controller.textBoxPressed(textBox)){
                font.getData().setScale(2.5f);
            }
        }
    }

    @Override
    public void dispose() {
        stage.dispose();
        batch.dispose();
    }
}
