package com.mygdx.game;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.scenes.scene2d.Actor;

import java.util.Random;

public class Ball extends Actor {
    private Sprite sprite;
    private float dirX;
    private float dirY;
    private int goStraightMod = 1;
    private float speedX;
    private float speedY;
    private int width;
    private int height;
    private float elapsedTime = 0;

    Ball (int width, int height) {
        Texture tex = new Texture("ball.jpg");
        sprite = new Sprite(tex, width, height);
        sprite.setBounds(sprite.getX(), sprite.getY(), width, height);
        this.width = width;
        this.height = height;
        sprite.setPosition(Gdx.graphics.getWidth()/2 - width/2, Gdx.graphics.getHeight()/2 - height/2);
        dirX = Math.random() > 0.5 ? 1 : -1;
        dirY = Math.random() > 0.5 ? 1 : -1;
        speedX = 300;
        speedY = 200 * (float) Math.random();
    }

    public void flipXDirection() {
        dirX *= -1;
    }

    public void flipYDirection() {
        dirY *= -1;
    }

    public void resetGame(){
        sprite.setPosition(Gdx.graphics.getWidth()/2 - width/2, Gdx.graphics.getHeight()/2 - height/2);
        dirX = Math.random() > 0.5 ? 1 : -1;
        dirY = Math.random() > 0.5 ? 1 : -1;
        speedX = 300;
        speedY = 200 * (float) Math.random();
        elapsedTime = 0;
    }

    public float getXPos() {
        return sprite.getX();
    }

    public float getYPos(){
        return sprite.getY();
    }

    public float getXDir(){
        return dirX;
    }

    public float getNextY(float delta){
        return getYPos() + (delta * speedY * dirY * goStraightMod);
    }

    public float getNextX(float delta) {
        return getXPos() + dirX * (delta * speedX);
    }

    public Rectangle getHitbox(){
        return sprite.getBoundingRectangle();
    }

    public Rectangle getNextHitbox(float delta) {
        return new Rectangle(getNextX(delta), getNextY(delta), sprite.getWidth(), sprite.getHeight());
    }

    public void setGoStraightMod(int mod){
        goStraightMod = mod;
    }

    @Override
    public void draw(Batch b, float a){
        sprite.draw(b);
    }

    @Override
    public void act(float delta){
        float nextY = getNextY(delta);

        elapsedTime += delta;

        if(elapsedTime > 10) {
            speedX *= 1.3;
            speedY *= 1.2;
            elapsedTime = elapsedTime % 10;
        }

        if(nextY < 0 || nextY > Gdx.graphics.getHeight() - sprite.getHeight()){
            flipYDirection();
        }

        sprite.setPosition(getNextX(delta), nextY);
    }
}
