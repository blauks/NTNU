package com.mygdx.game.models;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.scenes.scene2d.Actor;

// Model in MVC
public class Ball extends Actor {
    private Sprite sprite;
    private float dirX;
    private float dirY;
    private int goStraightMod = 1;
    private float speedX;
    private float speedY;
    private int width;
    private int height;
    private static Ball instance = new Ball(40, 40);

    private Ball (int width, int height) {
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

    public static Ball getInstance(){
        return instance;
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

    public Rectangle getNextHitbox(float delta) {
        return new Rectangle(getNextX(delta), getNextY(delta), sprite.getWidth(), sprite.getHeight());
    }

    public void setGoStraightMod(int mod){
        goStraightMod = mod;
    }

    public Sprite getSprite(){
        return sprite;
    }

    public float getSpeedX(){
        return speedX;
    }

    public void setSpeedX(float speed){
        speedX = speed;
    }

    public float getSpeedY(){
        return speedY;
    }

    public void setSpeedY(float speed){
        speedY = speed;
    }

    @Override
    public void draw(Batch b, float a){
        sprite.draw(b);
    }
}
