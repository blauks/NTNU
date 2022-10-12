package com.mygdx.game;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.scenes.scene2d.Actor;

public class Paddle extends Actor {
    private Sprite sprite;
    private boolean isAi = false;
    private int moveUpMod = 1;
    private int moveDownMod = 1;

    Paddle(float x, float y, int width, int height) {
        Texture tex = new Texture("hvit.jpg");
        sprite = new Sprite(tex, width, height);
        sprite.setBounds(sprite.getX(), sprite.getY(), width, height);
        sprite.setPosition(x, y);
    }

    Paddle(float x, float y, int width, int height, boolean isAi) {
        this.isAi = isAi;
        Texture tex = new Texture("hvit.jpg");
        sprite = new Sprite(tex, width, height);
        sprite.setBounds(sprite.getX(), sprite.getY(), width, height);
        sprite.setPosition(x, y);
    }

    public void humanMovement(float delta) {
        if (!Gdx.input.isTouched()) return;

        if ((sprite.getX() - 10 < Gdx.input.getX() && Gdx.input.getX() < Gdx.graphics.getWidth() / 2) || (sprite.getX() + 10 > Gdx.input.getX() && Gdx.graphics.getWidth() / 2 < Gdx.input.getX())) {
            if (Gdx.input.getY() < Gdx.graphics.getHeight() / 2 && sprite.getY() + sprite.getHeight() < Gdx.graphics.getHeight()) {
                sprite.setPosition(sprite.getX(), sprite.getY() + (delta * 150 * moveUpMod));
            } else if(Gdx.input.getY() > Gdx.graphics.getHeight() / 2 && sprite.getY() > 0) {
                sprite.setPosition(sprite.getX(), sprite.getY() - (delta * 150 * moveDownMod));
            }
        }
    }

    public void setPosition(float x, float y){
        sprite.setPosition(x, y);
    }

    public void aiMovement(float delta, float ballY) {
        float speed = ballY - (sprite.getY() + sprite.getHeight() / 2);
        if(speed >= 150) speed = 150;
        else if(speed <= -150) speed = -150;

        float nextY = sprite.getY() + speed * (delta);

        if(nextY > 0 && nextY + sprite.getHeight()< Gdx.graphics.getHeight()) {
            sprite.setPosition(sprite.getX(), nextY);
        }
    }

    public boolean isAi(){
        return isAi;
    }

    public float getXPos(){
        return sprite.getX();
    }

    public float getYPos(){
        return sprite.getY();
    }

    public float getHeight(){
        return sprite.getHeight();
    }

    public float getWidth(){
        return sprite.getWidth();
    }

    public Rectangle getHitbox(){
        return sprite.getBoundingRectangle();
    }

    public void setMoveUpMod(int mod){
        moveUpMod = mod;
    }

    public void setMoveDownMod(int mod){
        moveDownMod = mod;
    }

    @Override
    public void draw(Batch b, float alpha) {
        sprite.draw(b);
    }

    @Override
    public void act(float delta) {
        if (!isAi) {
            humanMovement(delta);
        }
    }
}
