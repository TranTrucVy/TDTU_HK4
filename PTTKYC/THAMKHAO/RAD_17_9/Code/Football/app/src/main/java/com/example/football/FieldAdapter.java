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

public class FieldAdapter extends RecyclerView.Adapter<FieldAdapter.MyViewHolder>{
    private Context context;
    private List<FieldFB> listField;
    private FieldClickListener listener;

    public FieldAdapter(Context context, List<FieldFB> listField, FieldClickListener listener) {
        this.context = context;
        this.listField = listField;
        this.listener = listener;
    }

    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new MyViewHolder(LayoutInflater.from(context).inflate(R.layout.row_field,parent,false));
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
        FieldFB field = listField.get(position);

        holder.field_name.setText(field.getField_name());
        holder.field_type.setText(field.getField_type());

        holder.layout_root.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                listener.onClick(listField.get(holder.getAdapterPosition()));
            }
        });
    }

    @Override
    public int getItemCount() {
        return listField.size();
    }

    public void filterList(List<FieldFB> containList) {
        listField = containList;
        notifyDataSetChanged();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder{

        LinearLayout layout_root;
        TextView field_name, field_type;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            layout_root = itemView.findViewById(R.id.layout_root);
            field_name = itemView.findViewById(R.id.field_name);
            field_type = itemView.findViewById(R.id.field_type);
        }
    }
}
