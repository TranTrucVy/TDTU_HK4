package com.example.football;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class HistoryAdapter extends RecyclerView.Adapter<HistoryAdapter.MyViewHolder> {
    private Context context;
    private List<PickDetail> lDetail;

    public HistoryAdapter(Context context, List<PickDetail> lDetail) {
        this.context = context;
        this.lDetail = lDetail;
    }

    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new HistoryAdapter.MyViewHolder(LayoutInflater.from(context).inflate(R.layout.row_history,parent,false));
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
        PickDetail pickDetail = lDetail.get(position);
        holder.his_nField.setText(pickDetail.getField_name());
        holder.his_tField.setText(pickDetail.getField_type().replace("Sân ",""));
        if(pickDetail.isTime_frame_1()) {
            holder.his_tFrame.setText("7h - 8h30");
        } else if (pickDetail.isTime_frame_2()) {
            holder.his_tFrame.setText("16h - 17h30");
        } else if (pickDetail.isTime_frame_3()) {
            holder.his_tFrame.setText("18h - 19h30");
        } else {
            holder.his_tFrame.setText("19h45 - 21h15");
        }
        holder.his_dPick.setText(pickDetail.getDate_order());
        holder.his_pPick.setText(pickDetail.getPrice());
    }

    @Override
    public int getItemCount() {
        return lDetail.size();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder{

        TextView his_nField, his_tField, his_tFrame, his_dPick, his_pPick;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            his_nField = itemView.findViewById(R.id.his_nField);
            his_tField = itemView.findViewById(R.id.his_tField);
            his_tFrame = itemView.findViewById(R.id.his_tFrame);
            his_dPick = itemView.findViewById(R.id.his_dPick);
            his_pPick = itemView.findViewById(R.id.his_pPick);
        }
    }
}
