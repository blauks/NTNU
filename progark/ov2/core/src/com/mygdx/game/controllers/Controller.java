package com.mygdx.game.controllers;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.mygdx.game.models.Ball;
import com.mygdx.game.models.Paddle;

import java.util.Locale;

// Controller of MVC
// Should handle all logic
public class Controller {
    private Paddle paddle1;
    private Paddle paddle2;
    private int score1 = 0;
    private int score2 = 0;
    private float elapsedTime = 0;
    private int maxScore = 1;
    private boolean gameUnderway = true;

    public Controller(Stage stage){
        paddle1 = new Paddle(10, Gdx.graphics.getHeight() / 2 - 150, 40, 300);
        paddle2 = new Paddle(Gdx.graphics.getWidth() - 50, Gdx.graphics.getHeight() / 2 - 150, 40, 300, true);

        stage.addActor(paddle1);
        stage.addActor(paddle2);
        stage.addActor(Ball.getInstance());
    }

    public void resetPositions() {
        setPaddleMods(1);
        Ball.getInstance().setGoStraightMod(1);
        Ball.getInstance().resetGame();
        paddle1.setPosition(10, Gdx.graphics.getHeight() / 2 - 150);
        paddle2.setPosition(Gdx.graphics.getWidth() - 50, Gdx.graphics.getHeight() / 2 - 150);
        elapsedTime = 0;
    }

    public void setPaddleMods(int mod) {
        paddle1.setMoveDownMod(mod);
        paddle1.setMoveUpMod(mod);
        paddle1.setMoveDownMod(mod);
        paddle2.setMoveUpMod(mod);
    }

    public void updateBallSpeed(Ball ball){
        ball.setSpeedX(ball.getSpeedX() * 1.3f);
        ball.setSpeedY(ball.getSpeedY() * 1.2f);
        elapsedTime = elapsedTime % 10;
    }

    public String getScoreboard(){
        return String.format(Locale.UK, "%d : %d", score1, score2);
    }

    public String getWinner(){
        return score1 == 21 ? "Player 1" : "Player 2";
    }

    public boolean getGameUnderway(){
        return gameUnderway;
    }

    public boolean textBoxPressed(Rectangle textBox){
        if (Gdx.input.isTouched() && textBox.contains(Gdx.input.getX(), Gdx.input.getY())) {
            score1 = 0;
            score2 = 0;
            return true;
        }
        return false;
    }

    public void render(float delta){
        if (score1 < maxScore && score2 < maxScore) {
            if (paddle1.isAi()) {
                PaddleController.aiMovement(delta, Ball.getInstance().getYPos() + (Ball.getInstance().getHeight() / 2), paddle1);
            }
            else{
                PaddleController.humanMovement(delta, paddle1);
            }

            if (paddle2.isAi()) {
                PaddleController.aiMovement(delta, Ball.getInstance().getYPos() + (Ball.getInstance().getHeight() / 2), paddle2);
            }
            else {
                PaddleController.humanMovement(delta, paddle2);
            }

            elapsedTime += delta;

            if(elapsedTime > 10){
                updateBallSpeed(Ball.getInstance());
            }

            BallController.moveBall(delta, Ball.getInstance());

            if (Ball.getInstance().getNextHitbox(delta).overlaps(paddle1.getHitbox()) || Ball.getInstance().getNextHitbox(delta).overlaps(paddle2.getHitbox())) {
                Ball.getInstance().flipXDirection();
            }

            if (Ball.getInstance().getXPos() >= Gdx.graphics.getWidth()) {
                score1 += 1;
                resetPositions();
            }

            if (Ball.getInstance().getXPos() <= 0) {
                score2 += 1;
                resetPositions();
            }
        }
        else {
            gameUnderway = false;
        }
    }
}
