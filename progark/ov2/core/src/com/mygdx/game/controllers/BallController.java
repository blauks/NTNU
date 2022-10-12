package com.mygdx.game.controllers;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.mygdx.game.models.Ball;

public class BallController {

    public static void moveBall(float delta,Ball ball){
        float nextY = ball.getNextY(delta);

        Sprite sprite = ball.getSprite();

        if(nextY < 0 || nextY > Gdx.graphics.getHeight() - sprite.getHeight()){
            ball.flipYDirection();
        }

        sprite.setPosition(ball.getNextX(delta), nextY);
    }
}
