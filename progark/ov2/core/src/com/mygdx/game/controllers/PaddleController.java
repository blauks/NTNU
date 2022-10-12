package com.mygdx.game.controllers;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.mygdx.game.models.Paddle;

public class PaddleController {

    public static void humanMovement(float delta, Paddle paddle){
        if (!Gdx.input.isTouched()) return;

        Sprite sprite = paddle.getSprite();

        if ((sprite.getX() - 10 < Gdx.input.getX() && Gdx.input.getX() < Gdx.graphics.getWidth() / 2) || (sprite.getX() + 10 > Gdx.input.getX() && Gdx.graphics.getWidth() / 2 < Gdx.input.getX())) {
            if (Gdx.input.getY() < Gdx.graphics.getHeight() / 2 && sprite.getY() + sprite.getHeight() < Gdx.graphics.getHeight()) {
                sprite.setPosition(sprite.getX(), sprite.getY() + (delta * 150 * paddle.getMoveUpMod()));
            } else if(Gdx.input.getY() > Gdx.graphics.getHeight() / 2 && sprite.getY() > 0) {
                sprite.setPosition(sprite.getX(), sprite.getY() - (delta * 150 * paddle.getMoveDownMod()));
            }
        }
    }

    public static void aiMovement(float delta, float ballY, Paddle paddle){
        Sprite sprite = paddle.getSprite();

        float speed = ballY - (sprite.getY() + sprite.getHeight() / 2);
        if(speed >= 150) speed = 150;
        else if(speed <= -150) speed = -150;

        float nextY = sprite.getY() + speed * (delta);

        if(nextY > 0 && nextY + sprite.getHeight()< Gdx.graphics.getHeight()) {
            sprite.setPosition(sprite.getX(), nextY);
        }
    }
}
