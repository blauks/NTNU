package com.mygdx.game;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Batch;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.scenes.scene2d.Actor;

public class Helicopter extends Actor {
    private Texture[] texes = {new Texture("heli1.png"), new Texture("heli2.png"), new Texture("heli3.png"), new Texture("heli4.png")};
    private Sprite sprite;
    private int dirX = 1;
    private int dirY = 1;
    private float speedX;
    private float speedY;
    private float timeElapsed = 0;
    private int curTex = 0;

    Helicopter(float speedX, float speedY) {
        this.speedX = speedX;
        this.speedY = speedY;
        sprite = new Sprite(texes[curTex]);
        setPosition(0, 0);
        setBounds(sprite.getX(), sprite.getY(), 130, 52);
        flipX();
    }

    Helicopter(float speedX, float speedY, float startX, float startY) {
        this.speedX = speedX;
        this.speedY = speedY;
        sprite = new Sprite(texes[curTex]);
        setPosition(startX, startY);
        setBounds(sprite.getX(), sprite.getY(), texes[0].getWidth(), texes[0].getHeight());
        flipX();
    }

    public void setPosition(float x, float y) {
        sprite.setPosition(x, y);
    }

    public void flipX() {
        sprite.flip(true, false);
    }

    public float getXPos() {
        return sprite.getX();
    }

    public float getYPos() {
        return sprite.getY();
    }

    public int getXDir(){
        return dirX;
    }

    public int getYDir(){
        return dirY;
    }

    public void flipXDir() {
        dirX *= -1;
        flipX();
    }

    public void stopHelicopter(){
        dirX = 0;
        dirY = 0;
    }

    public void flipYDir() {
        dirY *= -1;
    }

    public Rectangle getHitBox() {
        return sprite.getBoundingRectangle();
    }

    public float getWidth(){
        return sprite.getWidth();
    }

    public float getHeight(){
        return sprite.getHeight();
    }

    public float getNextXPos(float delta) {
        return getXPos() + (speedX * delta * dirX);
    }

    public float getNextYPos(float delta){
        return getYPos() + (speedY * delta * dirY);
    }

    public Rectangle getNextHitBox(float delta){
        return new Rectangle(getNextXPos(delta), getNextYPos(delta), sprite.getWidth(), sprite.getHeight());
    }

    @Override
    public void draw(Batch batch, float alpha) {
        sprite.draw(batch);
    }

    @Override
    public void act(float delta) {
        timeElapsed += delta;
        if (timeElapsed >= 0.1f) {
            curTex = (curTex + 1) % 4;
            sprite.setTexture(texes[curTex]);
        }

        float nextX = getNextXPos(delta);
        float nextY = getNextYPos(delta);
        boolean changedDirection = false;

        if (nextX < 0 || nextX + sprite.getWidth() > Gdx.graphics.getWidth()) {
            flipXDir();
            changedDirection = true;
        }

        if (nextY < 0 || nextY + sprite.getHeight() > Gdx.graphics.getHeight()) {
            flipYDir();
            changedDirection = true;
        }

        if (!changedDirection) {
            setPosition(nextX, nextY);
        }
    }
}
