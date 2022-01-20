package com.mygdx.game;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.scenes.scene2d.Actor;

public class Helicopter extends Actor {
    private Texture tex;
    private Sprite sprite;
    private float dirX = 1;
    private float dirY = 1;

    Helicopter (String imageLink) {
        tex = new Texture(imageLink);
        sprite = new Sprite(tex);
        setPosition(10,10);
        setBounds(0, 0, tex.getWidth(), tex.getHeight());
        flipX();
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
        float nextX = getXPos() + (100 * delta * dirX);
        float nextY = getYPos() + (100 * delta * dirY);
        boolean changedDirection = false;

        if(nextX < 0 || nextX + sprite.getWidth() > Gdx.graphics.getWidth()){
            dirX *= -1;
            flipX();
            changedDirection = true;
        }

        if(nextY < 0 || nextY + sprite.getHeight() > Gdx.graphics.getHeight()) {
            dirY *= -1;
            changedDirection = true;
        }

        if(!changedDirection) {
            setPosition(nextX, nextY);
        }
    }
}
