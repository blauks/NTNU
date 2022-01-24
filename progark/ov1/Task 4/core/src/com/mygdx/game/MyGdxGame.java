package com.mygdx.game;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.FitViewport;

import java.util.Locale;

public class MyGdxGame extends ApplicationAdapter {
    private Stage stage;
    private Helicopter[] heli;
    private SpriteBatch batch;

    @Override
    public void create() {
        batch = new SpriteBatch();

        FitViewport viewport = new FitViewport(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
        stage = new Stage(viewport, batch);
        Gdx.input.setInputProcessor(stage);

        heli = new Helicopter[]{new Helicopter(100, 100), new Helicopter(50, 400, 100, 100), new Helicopter(250, 10, 200, 400), new Helicopter(120, 300, 20, 700)};

        for (Helicopter h : heli) {
            stage.addActor(h);
        }
    }

    @Override
    public void render() {
        ScreenUtils.clear(0, 0, 0, 1);

        float delta = Gdx.graphics.getDeltaTime();

        stage.act(delta);
        stage.draw();

        for (int x = 0; x < heli.length - 1; x++) {
            for (int y = x + 1; y < heli.length; y++) {
                // Funker til en viss grad:D
                if (heli[x].getHitBox().overlaps(heli[y].getHitBox())) {
                    heli[x].flipYDir();
                    heli[x].flipXDir();
                    if(heli[x].getYDir() == heli[y].getYDir()){
                        heli[y].flipYDir();
                    }
                }
            }
        }
    }

    @Override
    public void dispose() {
        stage.dispose();
        batch.dispose();
    }
}
