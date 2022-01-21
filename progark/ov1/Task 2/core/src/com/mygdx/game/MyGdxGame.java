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
	private Helicopter heli;
	private BitmapFont font;
	private SpriteBatch batch;

	@Override
	public void create () {
		batch = new SpriteBatch();

		FitViewport viewport = new FitViewport(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
		stage = new Stage(viewport, batch);
		Gdx.input.setInputProcessor(stage);

		font = new BitmapFont();
		font.setColor(Color.WHITE);
		font.getData().setScale(2.5f);

		heli = new Helicopter("attackhelicopter.PNG");
		stage.addActor(heli);
	}

	@Override
	public void render () {
		ScreenUtils.clear(0, 0, 0, 1);

		stage.act(Gdx.graphics.getDeltaTime());
		stage.draw();

		batch.begin();
		font.draw(stage.getBatch(), String.format(Locale.UK, "x: %f, y: %f", heli.getXPos(), heli.getYPos()), 50, Gdx.graphics.getHeight() - 10);
		batch.end();
	}
	
	@Override
	public void dispose () {
		stage.dispose();
		batch.dispose();
	}
}
