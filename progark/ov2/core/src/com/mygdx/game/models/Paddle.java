package com.mygdx.game.models;

import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.scenes.scene2d.Actor;

// Model in MVC
public class Paddle extends Actor {
    private Sprite sprite;
    private boolean isAi = false;
    private int moveUpMod = 1;
    private int moveDownMod = 1;

    public Paddle(float x, float y, int width, int height) {
        Texture tex = new Texture("hvit.jpg");
        sprite = new Sprite(tex, width, height);
        sprite.setBounds(sprite.getX(), sprite.getY(), width, height);
        sprite.setPosition(x, y);
    }

    public Paddle(float x, float y, int width, int height, boolean isAi) {
        this.isAi = isAi;
        Texture tex = new Texture("hvit.jpg");
        sprite = new Sprite(tex, width, height);
        sprite.setBounds(sprite.getX(), sprite.getY(), width, height);
        sprite.setPosition(x, y);
    }

    public void setPosition(float x, float y){
        sprite.setPosition(x, y);
    }

    public boolean isAi(){
        return isAi;
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

    public Sprite getSprite(){
        return sprite;
    }

    public void setMoveUpMod(int mod){
        moveUpMod = mod;
    }

    public int getMoveUpMod(){
        return moveUpMod;
    }

    public void setMoveDownMod(int mod){
        moveDownMod = mod;
    }

    public int getMoveDownMod(){
        return moveDownMod;
    }

    @Override
    public void draw(Batch b, float alpha) {
        sprite.draw(b);
    }
}
