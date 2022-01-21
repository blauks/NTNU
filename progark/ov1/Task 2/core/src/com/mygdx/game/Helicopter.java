package com.mygdx.game;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.scenes.scene2d.Actor;
import com.badlogic.gdx.scenes.scene2d.InputEvent;
import com.badlogic.gdx.scenes.scene2d.InputListener;

public class Helicopter extends Actor {
    private Texture tex;
    private Sprite sprite;
    private float curDir = 1;
    private boolean move = false;

    Helicopter (String imageLink) {
        tex = new Texture(imageLink);
        sprite = new Sprite(tex);
        setPosition(0,0);
        setBounds(sprite.getX(), sprite.getY(), tex.getWidth(), tex.getHeight());
        flipX();

        addListener(new InputListener() {
            @Override
            public boolean touchDown (InputEvent event, float x, float y, int pointer, int button) {
                ((Helicopter)event.getTarget()).move = true;
                return true;
            }

            @Override
            public void touchUp (InputEvent event, float x, float y, int pointer, int button) {
                ((Helicopter)event.getTarget()).move = false;
            }
        });
    }

    public void setPosition(float x, float y){
        sprite.setPosition(x, y);
    }

    public void flipX(){
        sprite.flip(true, false);
    }

    public float getXPos(){
        return sprite.getX();
    }

    public float getYPos(){
        return sprite.getY();
    }

    @Override
    public void draw(Batch batch, float alpha){
        sprite.draw(batch);
    }

    @Override
    public void act(float delta){
        if (move){
            float nextX = getXPos() + ((Gdx.input.getX() - sprite.getWidth()/2  - getXPos()) * delta);
            float nextY = getYPos() + (((Gdx.graphics.getHeight() - Gdx.input.getY()) - sprite.getHeight()/2 - getYPos()) * delta);
            boolean outsideScreen = false;

            if ((nextX < 0 || nextX + sprite.getWidth() > Gdx.graphics.getWidth()) || (nextY < 0 || nextY + sprite.getHeight() > Gdx.graphics.getHeight())){
                outsideScreen = true;
            }

            if (nextX > sprite.getX() && curDir == 0){
                curDir = 1;
                sprite.flip(true, false);
            }
            else if (nextX < sprite.getX() && curDir == 1){
                curDir = 0;
                sprite.flip(true, false);
            }

            if(!outsideScreen){
                setBounds(sprite.getX(), sprite.getY(), tex.getWidth(), tex.getHeight());
                setPosition(nextX, nextY);
            }
        }
    }
}
