package com.mygdx.game;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.FitViewport;

import java.awt.Rectangle;

public class MyGdxGame extends ApplicationAdapter {
	private Stage stage;
	private Helicopter heli;

	@Override
	public void create () {
		FitViewport viewport = new FitViewport(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
		stage = new Stage(viewport);

		heli = new Helicopter("attackhelicopter.PNG");
		stage.addActor(heli);
	}

	@Override
	public void render () {
		ScreenUtils.clear(0, 0, 0, 1);
		stage.act(Gdx.graphics.getDeltaTime());
		stage.draw();
	}
	
	@Override
	public void dispose () {
		stage.dispose();
	}
}
